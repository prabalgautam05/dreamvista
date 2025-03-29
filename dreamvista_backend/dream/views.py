from django.shortcuts import render
from .gemini_api import interpret_dream
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Determine sentiment polarity using VADER."""
    scores = analyzer.polarity_scores(text)
    polarity = scores['compound']  # Compound score represents overall sentiment

    print(f"VADER Sentiment Score: {polarity}")  # Debugging

    if polarity >= 0.05:
        return "Positive 😊"
    elif polarity <= -0.05:
        return "Negative 😟"
    else:
        return "Neutral 😐"


def categorize_dream(dream_text):
    """Categorize the dream into types."""
    dream_text = dream_text.lower()

    print(f"Analyzing Dream Category for: {dream_text}")  # Debugging

    nightmare_keywords = [
        "scary", "fear", "chased", "monster", "dark", "haunted", "death", "screaming", 
        "witch", "ghost", "demon", "attack", "murder", "kill", "shadow", "curse", "blood"
    ]
    lucid_keywords = [
        "flying", "aware", "control", "lucid", "dream control", "awake in dream", "floating",
        "controlling", "astral projection", "seeing yourself"
    ]
    symbolic_keywords = [
        "symbol", "mystery", "hidden message", "prophetic", "spiritual", "sign", "premonition",
        "fortune", "vision", "prediction"
    ]

    if any(word in dream_text for word in nightmare_keywords):
        return "Nightmare 😱"
    elif any(word in dream_text for word in lucid_keywords):
        return "Lucid Dream ✨"
    elif any(word in dream_text for word in symbolic_keywords):
        return "Symbolic Dream 🔮"
    else:
        return "Uncategorized 💤"

def home(request):
    """Handle dream input, AI interpretation, sentiment, and categorization."""
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '').strip()

        if dream_text:
            interpretation = interpret_dream(dream_text)
            sentiment = analyze_sentiment(dream_text)
            category = categorize_dream(dream_text)

            print(f"Final Sentiment: {sentiment}, Category: {category}")  # Debugging

            return render(request, 'home.html', {
                'dream_text': dream_text,
                'interpretation': interpretation,
                'sentiment': sentiment,
                'category': category
            })

    return render(request, 'home.html')
