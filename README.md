# 🎬 Mood-Based Movie Recommendation System

A Flask web application that recommends movies based on the **user’s mood** using NLP and TMDB data.

The system detects emotions from text input, maps them to movie genres, and displays relevant movie suggestions stored in a local database.


🎥 Demo Video:  
https://drive.google.com/file/d/1pUqvYFe-zR8DQ_Qwc1UeH3h7z0Gb_dex/view?usp=sharing

---


<img height="300" alt="image" src="https://github.com/user-attachments/assets/252c0c7a-0b0f-4ba7-ac04-8241a6129eb1" />


---

## ✨ Features

* 🧠 Mood detection using HuggingFace NLP model
* 🎥 Movie recommendations based on detected emotion
* 🔎 Search movies by title
* 💾 SQLite database storage
* 🔄 Automatic data refresh every 15 days
* ⚡ Background initialization for faster startup
* 🌐 Flask web interface

---

## 🏗️ Project Structure

```
.
├── app.py                  # Main Flask application
├── db.py                   # Database setup and connection
├── fetch_tmdb.py           # TMDB API data fetching
├── Queries.py              # Database queries and logic
├── nlp_model.py            # Emotion detection model
├── mood_to_genres_map.py   # Mood → Genre mapping
├── templates/
│   └── index.html          # Frontend UI
└── movies.db               # SQLite database (auto-created)
```

Main application entry: app.py

---

## 🚀 How It Works

1. User enters text describing their mood.
2. NLP model detects emotion.
3. Emotion is mapped to movie genres.
4. Relevant movies are fetched from the database.
5. Results are displayed on the web page.

---

## 🧠 NLP Model

Uses:

```
j-hartmann/emotion-english-distilroberta-base
```

via HuggingFace Transformers pipeline.

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
https://github.com/smillingcoder/MovieChat.git
```

### 2️⃣ Install Dependencies

```bash
pip install requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

App will start at:

```
http://localhost:7860
```

---


## 🗄️ Database

* SQLite database (`movies.db`) is automatically created.
* Movie data is fetched from TMDB API on first run.
* Data refreshes every **15 days** automatically.

---


## 🛠️ Tech Stack

* Python
* Flask
* SQLite
* HuggingFace Transformers
* TMDB API
* HTML / CSS

---

## 👨‍💻 Author

Sohum Tiwari

GitHub: https://github.com/smillingcoder

---

## ⭐ If You Like This Project

Give it a star on GitHub ⭐
