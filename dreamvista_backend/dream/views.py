from django.shortcuts import render
from .gemini_api import interpret_dream

def home(request):
    if request.method == 'POST':
        dream_text = request.POST.get('dream_text', '')
        interpretation = interpret_dream(dream_text)
        return render(request, 'index.html', {'dream_text': dream_text, 'interpretation': interpretation})
    return render(request, 'index.html')
