from groq import Groq
from dreamvista_backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_interpretation(data):
    prompt = f"""
You are an expert dream analyst.

Analyze the dream and return output in STRICT plain text format.

IMPORTANT RULES:
- Do NOT use *, -, or any markdown symbols
- Do NOT use bullet points
- Use simple clean formatting
- Use headings like this:
- Keep each section concise (3-5 lines max).

Main Interpretation:
(text)

Emotional Meaning:
(text)

Symbolic Meaning:
(text)

Real-life Connection:
(text)

Dream: {data['text']}
Emotion: {data['emotion']}
Symbols: {', '.join(data['symbols'])}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating interpretation: {str(e)}"
