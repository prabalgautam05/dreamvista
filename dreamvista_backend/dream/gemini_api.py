import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def interpret_dream(dream_description):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(dream_description)
    return response.text
