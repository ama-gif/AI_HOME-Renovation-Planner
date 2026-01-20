"""Streamlit App for AI Home Renovation Planner
Deploy with: streamlit run app.py
"""

import streamlit as st
from pathlib import Path
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Home Renovation Planner",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #1f77b4;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Gemini API
if "api_key" not in st.session_state:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        st.session_state.api_key = api_key
    else:
        st.warning("⚠️ Please set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "model" not in st.session_state:
    st.session_state.model = genai.GenerativeModel('gemini-1.5-flash')
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Header
st.markdown('<div class="main-header">🏠 AI Home Renovation Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transform your space with AI-powered design recommendations</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📋 About")
    st.markdown("""
    This AI-powered tool helps you:
    - 📸 Analyze your current space
    - 🎨 Generate design recommendations
    - 💰 Estimate renovation costs
    - ⏱️ Create project timelines
    - 🖼️ Visualize your renovated space
    """)
    
    st.divider()
    
    st.header("🖼️ Upload Images")
    st.markdown("Upload photos of your current room or inspiration images")
    
    uploaded_files = st.file_uploader(
        "Choose images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    if uploaded_files:
        st.session_state.uploaded_files = uploaded_files
        st.success(f"✅ {len(uploaded_files)} image(s) uploaded")
        
        # Preview uploaded images
        st.subheader("Preview")
        cols = st.columns(2)
        for idx, file in enumerate(uploaded_files):
            with cols[idx % 2]:
                st.image(file, caption=file.name, use_container_width=True)
    
    st.divider()
    
    st.header("💡 Example Prompts")
    example_prompts = [
        "I want to renovate my kitchen",
        "Help me plan a bathroom update",
        "What's the average cost to renovate a bedroom?",
        "I have $15,000 to renovate my living room"
    ]
    
    for prompt in example_prompts:
        if st.button(prompt, key=f"example_{prompt}"):
            st.session_state.example_prompt = prompt
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.runner = Runner(root_agent)
        st.rerun()

# Main chat interface
chat_container = st.container()

with chat_container:
    # Display chat messages
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.markdown(f'<div class="chat-message user-message"><strong>You:</strong><br>{content}</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message assistant-message"><strong>Assistant:</strong><br>{content}</div>', 
                       unsafe_allow_html=True)
        
        # Display any images in the message
        if "images" in message and message["images"]:
            cols = st.columns(len(message["images"]))
            for idx, img_path in enumerate(message["images"]):
                with cols[idx]:
                    if os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)

# Chat input
user_input = st.chat_input("Describe your renovation project or ask a question...")

# Handle example prompt clicks
if "example_prompt" in st.session_state:
    user_input = st.session_state.example_prompt
    del st.session_state.example_prompt

# Process user input
if user_input:
    # Prepare message with uploaded files
    message_content = user_input
    image_paths = []
    
    # Save uploaded files temporarily
    if st.session_state.uploaded_files:
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        
        for file in st.session_state.uploaded_files:
            file_path = temp_dir / file.name
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            image_paths.append(str(file_path))
    
    # Add user message to chat
    st.session_state.messages.append({
        "role": "user",
        "content": message_content,
        "images": image_paths
    })
    
    # Display user message
    with chat_container:
        st.markdown(f'<div class="chat-message user-message"><strong>You:</strong><br>{message_content}</div>', 
                   unsafe_allow_html=True)
        
        if image_paths:
            cols = st.columns(len(image_paths))
            for idx, img_path in enumerate(image_paths):
                with cols[idx]:
                    st.image(img_path, use_container_width=True)
    
    # Get AI response
    with st.spinner("🤔 Analyzing your request..."):
        try:
            # Build message content
            content_parts = [message_content]
            
            # Add images if available
            if image_paths:
                for img_path in image_paths:
                    if os.path.exists(img_path):
                        with open(img_path, "rb") as img_file:
                            img_data = img_file.read()
                            # Add image to message
                            import base64
                            content_parts.append({
                                "mime_type": "image/jpeg" if img_path.endswith(('.jpg', '.jpeg')) else "image/png",
                                "data": base64.standard_b64encode(img_data).decode()
                            })
            
            # Get response from Gemini
            response = st.session_state.model.generate_content(content_parts)
            assistant_message = response.text if response else "Unable to generate response"
            
            # Add assistant message to chat
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_message,
                "images": []
            })
            
            # Clear uploaded files after processing
            st.session_state.uploaded_files = []
            
            # Rerun to update chat display
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.error("Please check your Gemini API configuration and credentials.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    Powered by Google Gemini & Streamlit
</div>
""", unsafe_allow_html=True)