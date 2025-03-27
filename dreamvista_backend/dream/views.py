from django.shortcuts import render
from .gemini_api import interpret_dream
from textblob import TextBlob

def analyze_sentiment(text):
    """Determine sentiment polarity of the dream."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😟"
    else:
        return "Neutral 😐"

def categorize_dream(dream_text):
    """Categorize the dream into types."""
    dream_text = dream_text.lower()
    if any(word in dream_text for word in ["scary", "fear", "chased", "monster", "dark", "haunted"]):
        return "Nightmare 😱"
    elif any(word in dream_text for word in ["flying", "aware", "control", "lucid", "dream control"]):
        return "Lucid Dream ✨"
    elif any(word in dream_text for word in ["symbol", "mystery", "hidden message", "prophetic"]):
        return "Symbolic Dream 🔮"
    else:
        return "Uncategorized 💤"

def home(request):
    """Handle dream input, AI interpretation, sentiment, and categorization."""
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '')
        if dream_text:
            interpretation = interpret_dream(dream_text)
            sentiment = analyze_sentiment(dream_text)
            category = categorize_dream(dream_text)

            return render(request, 'home.html', {
                'dream_text': dream_text,
                'interpretation': interpretation,
                'sentiment': sentiment,
                'category': category
            })

    return render(request, 'home.html')
