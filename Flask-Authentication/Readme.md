# Flask Authentication System

A simple user authentication web app built with Flask, featuring secure login, registration, and protected routes.

## Features

- User registration with hashed & salted passwords (`pbkdf2:sha256`)
- Login / logout with session management via Flask-Login
- Protected routes using `@login_required`
- SQLite database via SQLAlchemy ORM
- File download restricted to authenticated users

## Tech Stack

- **Backend:** Flask, Flask-Login, Flask-SQLAlchemy
- **Security:** Werkzeug password hashing
- **Database:** SQLite

## Setup

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
python main.py
```

App runs at `http://localhost:8080`

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home page |
| `/register` | GET, POST | Create a new account |
| `/login` | GET, POST | Login to existing account |
| `/secrets` | GET | Protected page (login required) |
| `/download` | GET | Download file (login required) |
| `/logout` | GET | Logout current user |

## Notes

- Replace `SECRET_KEY` in `app.config` with a secure random key before deploying.
- Passwords are never stored in plain text.
