# 📚 My Book Library

> A personal book collection manager built with Flask & SQLAlchemy.  
> Add, view, edit ratings, and delete books — all persisted in a local SQLite database.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📖 Overview

**My Book Library** is a lightweight full-stack web application that lets you manage your personal reading list.  
Built with **Flask** on the backend and a clean, responsive **HTML/CSS** frontend styled with a warm library theme.

---

## ✨ Features

- 📗 **Add Books** — Save title, author, and rating to the database
- 📋 **View All Books** — Responsive card-grid layout on the home page
- ✏️ **Edit Ratings** — Update a book's rating at any time
- 🗑️ **Delete Books** — Remove books from your collection
- 💾 **Persistent Storage** — SQLite database via Flask-SQLAlchemy
- 🎨 **Themed UI** — Warm library aesthetic with Google Fonts (Playfair Display + Lato)
- 🔁 **Full CRUD** — Complete Create, Read, Update, Delete functionality

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Backend     | Python, Flask                     |
| ORM         | Flask-SQLAlchemy, SQLAlchemy 2.x  |
| Database    | SQLite                            |
| Templating  | Jinja2                            |
| Frontend    | HTML5, CSS3 (no JS framework)     |
| Fonts       | Google Fonts                      |

---

## 📁 Project Structure

```
project/
├── main.py                        # Flask app, routes, DB models
├── requirements.txt               # Python dependencies
├── instance/
│   └── new-books-collection.db    # Auto-generated SQLite database
└── templates/
    ├── index.html                 # Home page — book card grid
    ├── add.html                   # Add new book form
    └── edit.html                  # Edit book rating form
```

---

## 🗄️ Database Schema

### `Book` Model

| Column   | Type        | Constraints                 |
|----------|-------------|-----------------------------|
| `id`     | Integer     | Primary Key, Auto-increment |
| `title`  | String(250) | Unique, Not Null            |
| `author` | String(250) | Not Null                    |
| `rating` | String      | Not Null                    |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/my-book-library.git
cd my-book-library
```

### 2. (Optional) Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
pip3 install -r requirements.txt
```

### 4. Run the App

```bash
python main.py
```

### 5. Open in Browser

```
http://localhost:8080
```

> The SQLite database (`new-books-collection.db`) is created automatically on first run inside the `instance/` folder.

---

## 📦 Dependencies

`requirements.txt`:

```
flask
flask-sqlalchemy
sqlalchemy
```

---

## 🚀 Usage

| Page           | URL            | Description                                  |
|----------------|----------------|----------------------------------------------|
| 🏠 Home        | `/`            | View all books in a card grid                |
| ➕ Add Book    | `/add`         | Fill in title, author & rating to add a book |
| ✏️ Edit Rating | `/edit?id=X`   | Update the rating of an existing book        |
| 🗑️ Delete      | `/delete?id=X` | Permanently remove a book from the library   |

---

## 🔀 API Routes

| Method | Route          | Description                     |
|--------|----------------|---------------------------------|
| `GET`  | `/`            | Render home page with all books |
| `GET`  | `/add`         | Render add book form            |
| `POST` | `/add`         | Submit new book to database     |
| `GET`  | `/edit?id=X`   | Render edit form for book `X`   |
| `POST` | `/edit`        | Update rating for book `X`      |
| `GET`  | `/delete?id=X` | Delete book `X` from database   |

---

## 🎨 Design

The UI uses a **warm library theme** with the following palette:

| Role         | Color     | Hex       |
|--------------|-----------|-----------|
| Primary Dark | Brown     | `#3b1f0a` |
| Secondary    | Mid Brown | `#6b3a1f` |
| Background   | Cream     | `#f5f0e8` |
| Accent       | Gold      | `#f0c060` |
| Card BG      | Off-white | `#fff8ee` |

**Fonts:** [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) (headings) · [Lato](https://fonts.google.com/specimen/Lato) (body)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**  
GitHub: [https://github.com/PavanRe001]

---

## 🙏 Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/)
- [Google Fonts](https://fonts.google.com/)
- [Shields.io](https://shields.io/) — for the badges
