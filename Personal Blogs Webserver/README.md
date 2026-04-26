# 📝 Flask Blog

A full-featured blog web application built with **Flask**, **SQLAlchemy**, and **CKEditor** — supporting rich-text post creation, editing, and deletion with a clean Bootstrap 5 UI.

---

## 🛠️ Tech Stack

- Python / Flask
- Flask-Bootstrap 5
- Flask-SQLAlchemy (SQLite)
- Flask-WTF (Forms)
- Flask-CKEditor (Rich Text Editor)

---

## ⚙️ Setup

1. **Clone the repo and install dependencies**
   ```bash
   pip install flask flask-bootstrap5 flask-sqlalchemy flask-wtf flask-ckeditor
   ```

2. **Run the server**
   ```bash
   python main.py
   ```
   The server will start at `http://127.0.0.1:5003`

---

## 🗄️ Database Model

The app uses a single `BlogPost` table:

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-incremented primary key |
| `title` | String(250) | Unique post title |
| `subtitle` | String(250) | Post subtitle |
| `date` | String(250) | Auto-set date on creation |
| `body` | Text | Rich HTML content via CKEditor |
| `author` | String(250) | Author's name |
| `img_url` | String(250) | Header image URL |

---

## 🌐 Routes

### 🏠 Home — All Posts
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Displays all blog posts |

**Example:**
```
GET http://127.0.0.1:5003/
```
Renders `index.html` with all posts fetched from the database.

---

### 📖 View a Single Post
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/post/<post_id>` | Displays a single blog post by ID |

**Example:**
```
GET http://127.0.0.1:5003/post/1
```
Renders `post.html` with the full content of the requested post.

---

### ✍️ Create a New Post
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/new-post` | Renders the new post form |
| POST | `/new-post` | Submits and saves a new post |

**Example:**
```
GET  http://127.0.0.1:5003/new-post
POST http://127.0.0.1:5003/new-post
```

**Form Fields:**

| Field | Validator | Description |
|-------|-----------|-------------|
| `title` | Required | Blog post title |
| `subtitle` | — | Short subtitle |
| `author` | Required | Author name |
| `img_url` | Required, Valid URL | Header image URL |
| `body` | — | Rich text body via CKEditor |

On success, redirects to `/` (home).

---

### ✏️ Edit an Existing Post
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/edit-post/<post_id>` | Renders the edit form pre-filled with existing data |
| POST | `/edit-post/<post_id>` | Submits and saves the updated post |

**Example:**
```
GET  http://127.0.0.1:5003/edit-post/1
POST http://127.0.0.1:5003/edit-post/1
```

On success, redirects to `/post/<post_id>` to view the updated post.

---

### 🗑️ Delete a Post
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/delete-post/<post_id>` | Deletes the post by ID and redirects home |

**Example:**
```
GET http://127.0.0.1:5003/delete-post/1
```

On success, redirects to `/` (home).

---


## 📁 Project Structure

```
.
├── main.py                  # Main Flask app
├── instance/
│   └── posts.db             # SQLite database (auto-created)
└── templates/
    ├── index.html           # Homepage — all posts
    ├── post.html            # Single post view
    ├── make-post.html       # Create / Edit post form
    ├── about.html           # About page
    └── contact.html         # Contact page
```

---

## 🚀 Quick Test (after running the server)

```bash
# View all posts
curl http://127.0.0.1:5003/

# View a specific post
curl http://127.0.0.1:5003/post/1

# Open new post form (browser)
open http://127.0.0.1:5003/new-post

# Open edit form for post ID 1 (browser)
open http://127.0.0.1:5003/edit-post/1

# Delete post ID 1
curl http://127.0.0.1:5003/delete-post/1
```
