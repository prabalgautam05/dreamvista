from transformers import pipeline

# Load once
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None  # 🔥 get all emotions
)


def detect_emotions(text):
    try:
        results = emotion_pipeline(text)[0]

        # Sort by confidence
        sorted_results = sorted(
            results, key=lambda x: x['score'], reverse=True)

        return sorted_results[:3]  # top 3 emotions

    except Exception:
        return [{"label": "neutral", "score": 1.0}]
