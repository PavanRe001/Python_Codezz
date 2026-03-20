# 🎬 Day 64 — My Top 10 Movies Website

> **100 Days of Code: The Complete Python Pro Bootcamp** — Angela Yu (Udemy)

---

## 📌 About the Project

A dynamic **Top 10 Movies** web application built using **Flask**, **SQLAlchemy**, and **WTForms**, integrated with the **The Movie Database (TMDb) API**. Users can search for movies, add them to a personal ranked list, edit their ratings and reviews, and delete entries — all stored in a local SQLite database.

This project was completed as part of **Day 64** of Angela Yu's 100 Days of Python Bootcamp, focusing on **Flask**, **relational databases with SQLAlchemy**, and **RESTful CRUD operations**.

---

## 🚀 Features

- 🔍 **Search Movies** — Live search using the TMDb API to find any movie
- ➕ **Add to List** — Select a movie from results and save it with a rating & review
- ✏️ **Edit Entries** — Update your rating and review anytime
- 🗑️ **Delete Movies** — Remove a movie from your list
- 🏆 **Auto Ranking** — Movies are automatically ranked by your rating (highest = #1)
- 🎨 **Movie Posters** — Fetched dynamically from TMDb API

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite via Flask-SQLAlchemy |
| Forms | Flask-WTForms |
| API | TMDb (The Movie Database) |
| Frontend | HTML5, CSS3, Bootstrap |
| Templating | Jinja2 |

---

## 📂 Project Structure

```
day-64-top-10-movies/
│
├── main.py              # Main Flask app with routes & DB models
├── forms.py             # WTForms for Add/Edit movie
├── templates/
│   ├── index.html       # Home page — ranked movie list
│   ├── add.html         # Search & add a movie
│   ├── edit.html        # Edit rating & review
│   └── select.html      # Select movie from TMDb results
├── static/
│   └── css/
│       └── style.css    # Custom styles
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/day-64-top-movies.git
cd day-64-top-movies
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up your TMDb API Key

Create a free account at [https://www.themoviedb.org/](https://www.themoviedb.org/) and get your API key.

Then set it as an environment variable or paste it directly in `main.py`:

```python
MOVIE_DB_API_KEY = "your_tmdb_api_key_here"
```

### 4. Run the app
```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser. 🎉

---

## 📸 Preview

![Top 10 Movies Website Screenshot](screenshot.png)

---

## 📚 Concepts Practiced

- Flask application factory & routing
- SQLAlchemy ORM — model creation, querying, updating, deleting
- WTForms — form validation and rendering
- External API integration (TMDb)
- Jinja2 templating with dynamic data
- Full CRUD operations in a web app

---

## 🙌 Acknowledgements

- [Angela Yu — 100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

> ⭐ If you found this helpful, consider giving this repo a star!
