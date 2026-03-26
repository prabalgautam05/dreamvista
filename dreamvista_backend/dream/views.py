from django.shortcuts import render
import re
from .services.dream_pipeline import analyze_dream_pipeline

FORBIDDEN_WORDS = [
    "news", "politics", "technology", "sports", "recipe", "weather", "tutorial",
    "how to", "current events", "stock market", "business trends"
]


def is_valid_dream(dream_text):
    dream_text = dream_text.lower()

    if any(word in dream_text for word in FORBIDDEN_WORDS):
        return False

    if not re.search(r"\bdream\b|\bsleep\b|\bdreamt\b|\bnight\b", dream_text):
        return False

    return True


def categorize_dream(text):
    text = text.lower()
    if "chased" in text or "attacked" in text or "witch" in text:
        return "Nightmare 😱"
    elif "flying" in text or "controlling" in text:
        return "Lucid Dream ✨"
    elif "ocean" in text or "animals" in text:
        return "Symbolic Dream 🔮"
    else:
        return "Uncategorized 💤"


def map_emotion_to_ui(emotion):
    emotion = emotion.lower()

    if emotion in ["joy", "happy"]:
        return "Positive 😊", 100, "bg-success"
    elif emotion in ["sadness", "fear", "anger"]:
        return "Negative 😟", 30, "bg-danger"
    else:
        return "Neutral 😐", 60, "bg-secondary"

def extract_structured_interpretation(text):
    sections = {
        "Main Interpretation": "",
        "Emotional Meaning": "",
        "Symbolic Meaning": "",
        "Real-life Connection": ""
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            continue

        if line.endswith(":") and line[:-1] in sections:
            current_section = line[:-1]
            continue

        if current_section:
            sections[current_section] += line + " "

    formatted_output = ""

    for title, content in sections.items():
        if content.strip():
            formatted_output += f"<br><b>{title}</b><br>"
            formatted_output += f"{content.strip()}<br>"

    return formatted_output


def index(request):

    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '').strip()

        if not is_valid_dream(dream_text):
            return render(request, 'index.html', {
                'error': "❌ Invalid input! Please describe a dream."
            })

        # ✅ Pipeline
        result = analyze_dream_pipeline(dream_text)

        # ✅ Emotion mapping
        emotion_label, sentiment_score, sentiment_class = map_emotion_to_ui(
            result["emotion"]
        )

        # ✅ Formatting
        formatted_interpretation = extract_structured_interpretation(
            result["interpretation"]
        )

        category = categorize_dream(dream_text)

        return render(request, 'index.html', {
            'dream_text': dream_text,
            'interpretation': formatted_interpretation,
            'sentiment': emotion_label,
            'sentiment_score': sentiment_score,
            'sentiment_class': sentiment_class,
            'category': category,
            'symbols': result["symbols"],
            'symbol_details': result["symbol_details"],
            'detected_emotion': result["emotion"],
            'emotions': result["emotions"],
            'similar_dreams': result["similar_dreams"]
        })

    return render(request, 'index.html')
