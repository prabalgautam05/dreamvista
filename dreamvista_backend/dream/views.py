from django.shortcuts import render
from .gemini_api import interpret_dream
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def home(request):
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '')
        interpretation = interpret_dream(dream_text)
        sentiment = analyze_sentiment(dream_text)
        return render(request, 'home.html', {
            'dream_text': dream_text,
            'interpretation': interpretation,
            'sentiment': sentiment
        })
    return render(request, 'home.html')
