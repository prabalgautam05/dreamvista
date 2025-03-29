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

    if any(word in dream_text for word in FORBIDDEN_WORDS):
        return False

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

def extract_structured_interpretation(text):
    """Extracts structured interpretation with proper formatting."""
    paragraphs = text.split('. ')  # Split into sentences
    structured_output = ""
    current_element = ""

    for sentence in paragraphs:
        sentence = sentence.strip()

        if ":" in sentence:  # Detect dream element (e.g., "The Witch:")
            current_element = sentence.split(":")[0].strip()
            structured_output += f"<br><b>{current_element}</b><br>"  # Proper bold element title

        elif current_element:  # Only add bullet points if an element is set
            structured_output += f"• {sentence.strip()}<br>"

    return structured_output

def index(request):
    """Handles dream input, AI interpretation, sentiment analysis, and categorization."""
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '').strip()

        if not is_valid_dream(dream_text):
            return render(request, 'index.html', {
                'error': "❌ Invalid input! Please describe a dream, not general topics."
            })

        interpretation = interpret_dream(dream_text)
        formatted_interpretation = extract_structured_interpretation(interpretation)  # Apply structured output
        sentiment, sentiment_score = analyze_sentiment(dream_text)
        category = categorize_dream(dream_text)

        return render(request, 'index.html', {
            'dream_text': dream_text,
            'interpretation': formatted_interpretation,  # Clean, structured output
            'sentiment': sentiment,
            'sentiment_score': sentiment_score,
            'category': category
        })

    return render(request, 'index.html')
