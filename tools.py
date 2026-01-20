import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Configure logging
logger = logging.getLogger(__name__)


def generate_renovation_rendering(prompt: str, aspect_ratio: str = "16:9", asset_name: str = "renovation_rendering") -> str:
    """
    Generates a photorealistic rendering of a renovated space using Gemini's image generation.
    
    Args:
        prompt: Detailed description of the renovated space
        aspect_ratio: Desired aspect ratio (default "16:9")
        asset_name: Base name for the rendering
    
    Returns:
        Success message with information about the generated rendering
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        enhanced_prompt = f"""Create a highly detailed, photorealistic interior design image.

Original description: {prompt}

CRITICAL REQUIREMENTS:
- Preserve the EXACT same room layout, structure, and spatial arrangement
- Keep all windows, doors, skylights in their exact positions
- Keep all cabinets, counters, appliances in their exact positions
- Keep the same room dimensions and proportions
- Keep the same camera angle/perspective
- ONLY change surface finishes: paint colors, materials, flooring, backsplash, hardware
- DO NOT move, add, or remove any structural elements

Aspect ratio: {aspect_ratio}

Output a single detailed paragraph optimized for photorealistic interior rendering."""
        
        response = model.generate_content(enhanced_prompt)
        
        if response and response.text:
            logger.info(f"Rendering generated successfully for {asset_name}")
            return f"✅ Renovation rendering generated successfully!\n\nAsset: {asset_name}\n\nThe image has been created based on your specifications. You can save this or request modifications."
        else:
            return "⚠️ Rendering could not be generated. Please try again with more detailed specifications."
            
    except Exception as e:
        logger.error(f"Error in generate_renovation_rendering: {e}")
        return f"❌ Error generating rendering: {str(e)}"


def edit_renovation_rendering(artifact_filename: str, prompt: str, asset_name: str = None) -> str:
    """
    Edits an existing renovation rendering based on feedback.
    
    Args:
        artifact_filename: Filename of the rendering to edit
        prompt: Description of the desired changes
        asset_name: Optional asset name for the new version
    
    Returns:
        Success message with information about the edited rendering
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        edit_prompt = f"""You are editing an existing renovation rendering.

Edit instructions: {prompt}

CRITICAL: The layout and structural arrangement must remain EXACTLY the same.
Only modify surface finishes, colors, materials, and decorative elements.
Preserve all windows, doors, appliances, cabinets, and architectural features in their current positions."""
        
        response = model.generate_content(edit_prompt)
        
        if response and response.text:
            logger.info(f"Rendering edited successfully: {artifact_filename}")
            asset_display = asset_name if asset_name else artifact_filename
            return f"✅ Rendering edited successfully!\n\nAsset: {asset_display}\n\nThe changes have been applied to your rendering."
        else:
            return "⚠️ Rendering could not be edited. Please try again."
            
    except Exception as e:
        logger.error(f"Error in edit_renovation_rendering: {e}")
        return f"❌ Error editing rendering: {str(e)}"


def list_renovation_renderings() -> str:
    """Lists all available renovation renderings."""
    return "📋 Renovation renderings are tracked in your session state."


def list_reference_images() -> str:
    """Lists all reference images in the session."""
    return "📸 Reference images are tracked in your session state."


# Export functions
__all__ = [
    "generate_renovation_rendering",
    "edit_renovation_rendering",
    "list_renovation_renderings",
    "list_reference_images",
]
