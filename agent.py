import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)


# Helper function for cost estimation
def estimate_renovation_cost(
    room_type: str,
    scope: str,
    square_footage: int,
) -> str:
    """Estimate renovation costs based on room type and scope.
    
    Args:
        room_type: Type of room (kitchen, bathroom, bedroom, living_room, etc.)
        scope: Renovation scope (cosmetic, moderate, full, luxury)
        square_footage: Room size in square feet
    
    Returns:
        Estimated cost range
    """
    # Cost per sq ft estimates (2024 ranges)
    rates = {
        "kitchen": {"cosmetic": (50, 100), "moderate": (150, 250), "full": (300, 500), "luxury": (600, 1200)},
        "bathroom": {"cosmetic": (75, 125), "moderate": (200, 350), "full": (400, 600), "luxury": (800, 1500)},
        "bedroom": {"cosmetic": (30, 60), "moderate": (75, 150), "full": (150, 300), "luxury": (400, 800)},
        "living_room": {"cosmetic": (40, 80), "moderate": (100, 200), "full": (200, 400), "luxury": (500, 1000)},
    }
    
    room = room_type.lower().replace(" ", "_")
    scope_level = scope.lower()
    
    if room not in rates:
        room = "living_room"
    if scope_level not in rates[room]:
        scope_level = "moderate"
    
    low, high = rates[room][scope_level]
    
    total_low = low * square_footage
    total_high = high * square_footage
    
    return f"💰 Estimated Cost: ${total_low:,} - ${total_high:,} ({scope_level} {room_type} renovation, ~{square_footage} sq ft)"


def calculate_timeline(
    scope: str,
    room_type: str,
) -> str:
    """Estimate renovation timeline based on scope and room type.
    
    Args:
        scope: Renovation scope (cosmetic, moderate, full, luxury)
        room_type: Type of room being renovated
    
    Returns:
        Estimated timeline with phases
    """
    timelines = {
        "cosmetic": "1-2 weeks (quick refresh)",
        "moderate": "3-6 weeks (includes some structural work)",
        "full": "2-4 months (complete transformation)",
        "luxury": "4-6 months (custom work, high-end finishes)"
    }
    
    scope_level = scope.lower()
    timeline = timelines.get(scope_level, timelines["moderate"])
    
    return f"⏱️ Estimated Timeline: {timeline}"


# Create renovation planner agent
def create_renovation_plan(user_message: str, images=None):
    """Create a comprehensive renovation plan using Gemini."""
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    system_prompt = """You are an expert AI Home Renovation Planner. Help users plan their home renovations by:
1. Analyzing current space photos and inspiration images
2. Providing design recommendations
3. Estimating renovation costs
4. Creating project timelines
5. Suggesting materials and finishes
6. Offering budget-friendly alternatives

Be enthusiastic, detailed, and practical in your recommendations. Ask clarifying questions when needed."""
    
    # Build the conversation
    try:
        response = model.generate_content(
            [system_prompt, user_message],
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=2048,
            )
        )
        return response.text
    except Exception as e:
        return f"Error generating renovation plan: {str(e)}"


# Export the main agent
root_agent = {
    "estimate_cost": estimate_renovation_cost,
    "calculate_timeline": calculate_timeline,
    "create_plan": create_renovation_plan,
}

__all__ = ["root_agent", "estimate_renovation_cost", "calculate_timeline", "create_renovation_plan"]