import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_model(model_name: str = "gemini-1.5-flash"):
    """
    Initializes and returns the Gemini model.
    Default is gemini-1.5-flash for speed and cost-effectiveness.
    """
    return genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": 0.2,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "application/json",
        }
    )
