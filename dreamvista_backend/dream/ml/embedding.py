from sentence_transformers import SentenceTransformer
import numpy as np
from ..models import Dream

model = SentenceTransformer('all-MiniLM-L6-v2')


def generate_embedding(text):
    return model.encode(text).tolist()


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def add_dream_to_db(text):
    embedding = generate_embedding(text)

    Dream.objects.create(
        text=text,
        embedding=embedding
    )


def find_similar_dreams(text, top_k=3):
    query_embedding = generate_embedding(text)

    dreams = Dream.objects.all()

    similarities = []

    for dream in dreams:
        sim = cosine_similarity(query_embedding, dream.embedding)
        similarities.append((sim, dream.text))

    similarities.sort(reverse=True)

    return [text for _, text in similarities[:top_k]]
