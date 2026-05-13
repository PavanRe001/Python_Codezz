# Flask Blog

A multi-user blog platform built with Flask, featuring authentication, rich-text posts, comments, and admin controls.

## Features

- User registration & login with hashed passwords (`pbkdf2:sha256`)
- Admin-only controls for creating, editing, and deleting posts
- Rich-text post editor via CKEditor
- Commenting system for authenticated users
- Gravatar avatars for commenters
- Relational database with Users, Posts, and Comments

## Tech Stack

- **Backend:** Flask, Flask-Login, Flask-SQLAlchemy, Flask-CKEditor
- **Frontend:** Bootstrap 5
- **Security:** Werkzeug password hashing
- **Database:** SQLite

## Setup

```bash
pip install -r requirements.txt
python main.py
```

App runs at `http://localhost:8080`

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | All blog posts |
| `/register` | GET, POST | Create a new account |
| `/login` | GET, POST | Login |
| `/logout` | GET | Logout |
| `/post/<id>` | GET, POST | View post & add comments |
| `/new-post` | GET, POST | Create post (admin only) |
| `/edit-post/<id>` | GET, POST | Edit post (admin only) |
| `/delete/<id>` | GET | Delete post (admin only) |
| `/about` | GET | About page |
| `/contact` | GET | Contact page |

## Notes

- The first registered user (id=1) is automatically the admin.
- Replace `SECRET_KEY` in `app.config` with a secure random key before deploying.
