# 🌙 DreamVista – AI-Powered Dream Interpretation System 🔮

DreamVista is an advanced AI-driven web application that analyzes and interprets dreams using a hybrid architecture combining **Machine Learning, Natural Language Processing, and Large Language Models (LLMs)**.

It goes beyond basic chatbot responses by integrating **emotion detection, symbol intelligence, and semantic similarity search**, creating a personalized and insightful dream analysis experience.

---

# 🚀 Features

## 🧠 1. Multi-Emotion Detection

* Uses transformer-based NLP model
* Detects **top 3 emotions** with confidence scores
* Provides deeper psychological insight into dreams

## 🔮 2. Dream Symbol Intelligence

* Extracts key symbols (e.g., falling, snake, water)
* Maps each symbol to psychological meaning
* Enhances interpretability and user understanding

## 🤖 3. AI-Powered Dream Interpretation

* Uses LLM (via Groq API)
* Generates structured explanations:

  * Main Interpretation
  * Emotional Meaning
  * Symbolic Meaning
  * Real-life Connection

## 🧬 4. Similar Dreams Engine (Core Feature)

* Converts dreams into vector embeddings
* Finds similar dreams using cosine similarity
* Works like a **recommendation system**

## 💾 5. Persistent Dream Memory

* Stores dreams + embeddings in database
* Enables:

  * Long-term analysis
  * Pattern detection
  * Personalization

## 📊 6. Dynamic Emotion Visualization

* Displays emotion confidence using progress bars
* Provides intuitive UI feedback

## 🎨 7. Clean UI + UX

* Bootstrap-based responsive design
* Dark mode support 🌙
* Structured interpretation display

---

# 🧠 System Architecture

```
User Input
   ↓
Preprocessing & Validation
   ↓
Emotion Detection (Transformer Model)
   ↓
Symbol Extraction Engine
   ↓
Embedding Generation (MiniLM)
   ↓
Similarity Search (Database)
   ↓
LLM (Groq) → Interpretation
   ↓
Frontend Rendering
```

---

# ⚙️ Tech Stack

## Backend

* Django (Python)
* SQLite (default DB)

## AI / ML

* Transformers (HuggingFace)
* Sentence Transformers (MiniLM)
* Cosine Similarity (NumPy)

## LLM

* Groq API (LLaMA-based models)

## Frontend

* HTML, CSS, Bootstrap
* JavaScript


# 🔧 Installation & Setup

## 1. Clone Repository

```
git clone <your-repo-url>
cd dreamvista_backend
```

## 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install django transformers torch sentence-transformers groq numpy
```

---

## 4. Add API Key

📁 `config.py`

```
GROQ_API_KEY = "your_api_key_here"
```

---

## 5. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Run Server

```
python manage.py runserver
```

---

# 🧠 Core Modules Explained

## 🔹 Emotion Detection

* Model: `distilroberta-based emotion classifier`
* Returns top 3 emotions with scores

---

## 🔹 Embedding System

* Model: `all-MiniLM-L6-v2`
* Converts text → vector
* Used for similarity search

---

## 🔹 Similar Dreams Algorithm

```
similarity = dot(A, B) / (||A|| * ||B||)
```

* Uses cosine similarity
* Retrieves top K closest dreams

---

## 🔹 Dream Pipeline

Handles:

* Emotion detection
* Symbol extraction
* LLM interpretation
* Similarity search

---

# 📊 Example Output

```
Emotion:
- Fear (72%)
- Sadness (18%)
- Surprise (10%)

Symbols:
- Falling → insecurity
- Dark → uncertainty

Interpretation:
Main Interpretation:
You are experiencing uncertainty...

Real-life Connection:
This may relate to decisions...
```

---

# ⚡ Key Highlights

* Hybrid AI system (ML + LLM)
* Real-time inference
* Data-driven similarity engine
* Scalable architecture

---

# 🚀 Future Enhancements

## 🔥 Planned Features

* 📊 Emotion Analytics Dashboard
* 🧬 Personalized Dream Profile
* 🧠 Memory-based AI Assistant
* 🔗 Integration with Nexus AI system
* 📈 Dream Pattern Prediction

---

# 🧠 Learning Outcomes

This project demonstrates:

* NLP pipeline design
* Transformer model integration
* Embedding-based search systems
* Backend architecture (Django)
* Real-world AI product design

---

# 🤝 Contribution

Contributions are welcome!

1. Fork repo
2. Create feature branch
3. Submit PR

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 🌟 Final Note

DreamVista is not just a project —
it’s a step toward building **emotionally intelligent AI systems**.

---

**Built with ❤️ using AI & Django**
