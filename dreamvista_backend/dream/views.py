import re
from django.shortcuts import render
from .gemini_api import interpret_dream
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# 🚫 Restricted non-dream-related keywords
FORBIDDEN_WORDS = [
    "news", "politics", "technology", "sports", "recipe", "weather", "tutorial",
    "how to", "current events", "stock market", "business trends"
]

def is_valid_dream(dream_text):
    """Validate if input is a real dream description."""
    dream_text = dream_text.lower()

    # 🚨 Block queries with forbidden words
    if any(word in dream_text for word in FORBIDDEN_WORDS):
        return False

    # 💤 Ensure dream-related context
    if not re.search(r"\bdream\b|\bsleep\b|\bdreamt\b|\bnight\b", dream_text):
        return False
    
    return True

def analyze_sentiment(text):
    """Perform sentiment analysis using Vader."""
    score = analyzer.polarity_scores(text)['compound']
    
    if score >= 0.05:
        return "Positive 😊", 100  # Full progress bar
    elif score <= -0.05:
        return "Negative 😟", 20  # Small progress bar
    else:
        return "Neutral 😐", 50  # Mid-sized progress bar

def categorize_dream(text):
    """Basic categorization based on keywords."""
    text = text.lower()
    if "chased" in text or "attacked" in text or "witch" in text:
        return "Nightmare 😱"
    elif "flying" in text or "controlling" in text:
        return "Lucid Dream ✨"
    elif "ocean" in text or "animals" in text:
        return "Symbolic Dream 🔮"
    else:
        return "Uncategorized 💤"

def format_interpretation(text):
    """Break AI-generated interpretation into readable sub-paragraphs."""
    sentences = text.split('. ')  # Split long text into sentences
    formatted_text = ""

    for sentence in sentences:
        if len(sentence.strip()) > 0:
            formatted_text += f"<p>✅ {sentence.strip()}.</p>\n"  # Wrap each sentence in a paragraph
    
    return formatted_text

def home(request):
    """Handles dream input, AI interpretation, sentiment analysis, and categorization."""
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '').strip()

        if not is_valid_dream(dream_text):
            return render(request, 'home.html', {
                'error': "❌ Invalid input! Please describe a dream, not general topics."
            })

        interpretation = interpret_dream(dream_text)
        formatted_interpretation = format_interpretation(interpretation)  # Apply structured formatting
        sentiment, sentiment_score = analyze_sentiment(dream_text)
        category = categorize_dream(dream_text)

        return render(request, 'home.html', {
            'dream_text': dream_text,
            'interpretation': formatted_interpretation,  # Send formatted output
            'sentiment': sentiment,
            'sentiment_score': sentiment_score,
            'category': category
        })

    return render(request, 'home.html')
