# AI_HOME-Renovation-Planner
# AI HOME Renovation Planner

An intelligent home renovation planning assistant powered by Google Gemini AI that helps homeowners plan, visualize, and estimate their renovation projects through an interactive chat interface.

## 🏠 Overview

AI HOME Renovation Planner is a Streamlit-based application that leverages Google's Gemini AI to assist users in planning their home renovation projects. Upload photos of your space, describe your vision, and get personalized recommendations, cost estimates, timelines, and design suggestions.

## ✨ Features

- **📸 Image Analysis**: Upload photos of your current space for AI-powered analysis
- **🎨 Design Recommendations**: Get personalized design suggestions based on your preferences and space
- **💰 Smart Cost Estimation**: Receive detailed budget estimates for different renovation scopes
- **⏱️ Project Timeline Planning**: Get realistic timelines for your renovation project
- **🖼️ Photorealistic Renderings**: Generate visualizations of your renovated space
- **💬 Interactive Chat Interface**: Natural conversation with the AI assistant
- **🎯 Multiple Renovation Scopes**: Support for cosmetic, moderate, full, and luxury renovations
- **🏡 Multi-Room Support**: Kitchen, bathroom, bedroom, living room, and more

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Google Gemini AI**: Advanced AI model for natural language processing and image analysis
- **Streamlit**: Modern web framework for the interactive UI
- **python-dotenv**: Environment variable management
- **Pillow**: Image processing capabilities

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ama-gif/AI_HOME-Renovation-Planner.git
   cd AI_HOME-Renovation-Planner
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   # Or alternatively:
   # GOOGLE_API_KEY=your_google_api_key_here
   ```

## 💻 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   
   The application will automatically open in your browser at:
   ```
   http://localhost:8501
   ```

3. **Start planning your renovation**
   - Upload photos of your current space using the sidebar
   - Describe your renovation goals in the chat
   - Ask questions about costs, materials, and timelines
   - Get personalized recommendations and visualizations

## 📁 Project Structure

```
AI_HOME-Renovation-Planner/
├── app.py              # Main Streamlit application
├── agent.py            # Gemini AI agent and helper functions
├── tools.py            # Rendering generation and editing tools
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # Project documentation
```

## 🔧 Core Components

### `app.py`
The main Streamlit application that provides:
- Interactive chat interface with custom styling
- Image upload and preview functionality
- Session state management
- Integration with Gemini AI for responses

### `agent.py`
AI agent implementation featuring:
- **Cost Estimation**: Calculate renovation costs based on room type, scope, and square footage
- **Timeline Calculation**: Estimate project duration for different renovation scopes
- **Renovation Planning**: Generate comprehensive renovation plans using Gemini AI

### `tools.py`
Advanced rendering tools including:
- **Photorealistic Rendering Generation**: Create detailed visualizations of renovated spaces
- **Rendering Editing**: Modify existing renderings based on feedback
- **Asset Management**: Track and manage renovation renderings

## 💡 Example Use Cases

### Cost Estimation
```
User: "How much would it cost to do a moderate kitchen renovation for a 150 sq ft space?"
AI: Estimates $22,500 - $37,500 with detailed breakdown
```

### Design Planning
```
User: "I want to update my bathroom with modern finishes"
AI: Provides material suggestions, color schemes, and layout recommendations
```

### Project Timeline
```
User: "How long would a full bedroom renovation take?"
AI: Estimates 2-4 months with phase breakdown
```

## 🎯 Renovation Scopes

The application supports four renovation scope levels:

- **Cosmetic** (1-2 weeks): Paint, fixtures, minor updates
- **Moderate** (3-6 weeks): Includes some structural work, new finishes
- **Full** (2-4 months): Complete transformation, major changes
- **Luxury** (4-6 months): Custom work, high-end finishes, premium materials

## 🏠 Supported Room Types

- Kitchen
- Bathroom
- Bedroom
- Living Room
- And more...

## 📊 Cost Estimation Ranges (2024)

| Room Type | Cosmetic | Moderate | Full | Luxury |
|-----------|----------|----------|------|--------|
| Kitchen | $50-100/sqft | $150-250/sqft | $300-500/sqft | $600-1200/sqft |
| Bathroom | $75-125/sqft | $200-350/sqft | $400-600/sqft | $800-1500/sqft |
| Bedroom | $30-60/sqft | $75-150/sqft | $150-300/sqft | $400-800/sqft |
| Living Room | $40-80/sqft | $100-200/sqft | $200-400/sqft | $500-1000/sqft |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Add support for more room types
- Enhance cost estimation algorithms
- Improve UI/UX design
- Add export functionality for renovation plans
- Integrate with home design APIs

## 🐛 Troubleshooting

**API Key Issues**
- Ensure your Gemini API key is correctly set in the `.env` file
- Check that the key has the necessary permissions

**Image Upload Problems**
- Supported formats: JPG, JPEG, PNG
- Check file size (large files may take longer to process)

**Installation Issues**
- Ensure Python 3.8+ is installed
- Try upgrading pip: `pip install --upgrade pip`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**ama-gif**
- GitHub: [@ama-gif](https://github.com/ama-gif)

## 🙏 Acknowledgments

- Google Gemini AI for powerful natural language and image processing
- Streamlit for the intuitive web framework
- The open-source community for inspiration and support

## 📧 Support

For questions, suggestions, or issues:
- Open an issue on [GitHub](https://github.com/ama-gif/AI_HOME-Renovation-Planner/issues)
- Check existing issues for solutions

## 🚀 Future Enhancements

- [ ] 3D room visualization
- [ ] Material cost database integration
- [ ] Contractor matching service
- [ ] Before/after comparison gallery
- [ ] PDF export for renovation plans
- [ ] Multi-language support
- [ ] Mobile app version

---

**Transform Your Space with AI! 🏡✨**

Made with ❤️ using Google Gemini & Streamlit
