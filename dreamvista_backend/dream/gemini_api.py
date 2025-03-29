import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def interpret_dream(dream_description):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(dream_description)
    return response.text
