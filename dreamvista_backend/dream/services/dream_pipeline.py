from ..ml.emotion import detect_emotions
from ..ml.embedding import add_dream_to_db, find_similar_dreams
from ..llm.groq_client import generate_interpretation

SYMBOLS = {
    "falling": "insecurity",
    "flying": "freedom",
    "snake": "fear or transformation",
    "water": "emotions",
    "dark": "uncertainty",
    "chased": "avoidance",
    "death": "change",
    "fire": "anger",
    "baby": "new beginnings"
}

SYMBOL_MEANINGS = {
    "falling": "You may feel a lack of control or fear of failure.",
    "flying": "Represents freedom and ambition.",
    "snake": "Fear, danger, or transformation.",
    "water": "Deep emotions or subconscious mind.",
    "dark": "Fear of unknown or uncertainty.",
    "chased": "Avoiding a situation.",
    "death": "End of a phase or transformation.",
    "fire": "Anger or strong emotions.",
    "baby": "New beginnings or ideas."
}


def extract_symbols(text):
    text = text.lower()
    found = []

    for key in SYMBOLS:
        if key in text:
            found.append(key)

    return found if found else ["general dream"]


def analyze_dream_pipeline(text):
    # 🔥 multi-emotion detection
    emotions = detect_emotions(text)
    primary_emotion = emotions[0]["label"]

    symbols = extract_symbols(text)

    symbol_details = {
        symbol: SYMBOL_MEANINGS.get(symbol, "General subconscious symbol")
        for symbol in symbols
    }

    interpretation = generate_interpretation({
        "text": text,
        "emotion": primary_emotion,
        "symbols": symbols
    })

    # Find similar dreams
    similar_dreams = find_similar_dreams(text)

# Save current dream
    add_dream_to_db(text)

    return {
        "emotion": primary_emotion,
        "emotions": emotions,
        "symbols": symbols,
        "symbol_details": symbol_details,
        "interpretation": interpretation,
        "similar_dreams": similar_dreams
    }
