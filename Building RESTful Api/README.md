# ☕ Cafe & Wifi API

A RESTful API built with **Flask** and **SQLAlchemy** that lets you explore, add, update, and delete cafes — complete with amenity info like WiFi, sockets, toilets, and coffee prices.

---
> 📬 **[View Postman Documentation](https://documenter.getpostman.com/view/53428798/2sBXijLCui#90d8315a-1868-4aed-889f-82588c93e5d4)**
## 🛠️ Tech Stack

- Python / Flask
- Flask-SQLAlchemy (SQLite)
- python-dotenv

---

## ⚙️ Setup

1. **Clone the repo and install dependencies**
   ```bash
   pip install flask flask-sqlalchemy python-dotenv
   ```

2. **Create a `.env` file** in the root directory and add your secret API key:
   ```
   API_KEY=your_secret_key_here
   ```

3. **Run the server**
   ```bash
   python main.py
   ```
   The server will start at `http://127.0.0.1:8080`

---

## 📡 API Endpoints

### 🏠 Home
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Renders the homepage |

**Example:**
```
GET http://127.0.0.1:8080/
```

---

### 🎲 Get a Random Cafe
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/random` | Returns a randomly selected cafe |

**Example:**
```
GET http://127.0.0.1:8080/random
```

**Sample Response:**
```json
{
  "cafe": {
    "name": "The Brew Lab",
    "map_url": "https://maps.google.com/?q=brew+lab",
    "img_url": "https://example.com/brew.jpg",
    "location": "London",
    "amenities": {
      "seats": "40-50",
      "has_toilet": true,
      "has_wifi": true,
      "has_sockets": true,
      "can_take_calls": false,
      "coffee_price": "£2.80"
    }
  }
}
```

---

### 📋 Get All Cafes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/all` | Returns all cafes sorted alphabetically by name |

**Example:**
```
GET http://127.0.0.1:8080/all
```

**Sample Response:**
```json
{
  "cafes": {
    "cafes": [
      {
        "id": 1,
        "name": "Aroma House",
        "location": "Manchester",
        "coffee_price": "£3.00",
        "has_wifi": true,
        ...
      }
    ]
  }
}
```

---

### 🔍 Search Cafes by Location
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/search?loc={location}` | Returns all cafes at a given location |

**Example:**
```
GET http://127.0.0.1:8080/search?loc=London
```

**Sample Response:**
```json
{
  "cafes": {
    "cafes": [
      {
        "id": 3,
        "name": "The Brew Lab",
        "location": "London",
        ...
      }
    ]
  }
}
```

**If not found:**
```json
{
  "error": {
    "Not Found": "Sorry, we don't have a cafe at that location."
  }
}
```

---

### ➕ Add a New Cafe
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/add` | Adds a new cafe to the database |

**Example (form-data body):**
```
POST http://127.0.0.1:8080/add
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Cafe name |
| `map_url` | string | Google Maps URL |
| `img_url` | string | Image URL |
| `loc` | string | Location/City |
| `sockets` | bool | Has power sockets? |
| `toilet` | bool | Has toilet? |
| `wifi` | bool | Has WiFi? |
| `calls` | bool | Can take calls? |
| `seats` | string | Number of seats (e.g. `"20-30"`) |
| `coffee_price` | string | Price (e.g. `"£2.50"`) |

**Sample Response:**
```json
{
  "response": {
    "success": "Successfully added the new cafe."
  }
}
```

---

### 💰 Update Coffee Price
| Method | Endpoint | Description |
|--------|----------|-------------|
| PATCH | `/update-price/{cafe_id}?new_price={price}` | Updates the coffee price for a cafe by ID |

**Example:**
```
PATCH http://127.0.0.1:8080/update-price/3?new_price=£3.50
```

**Sample Response:**
```json
{
  "response": {
    "success": "Successfully updated the price."
  }
}
```

**If cafe not found:**
```json
{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
```

---

### 🗑️ Delete a Cafe (Report as Closed)
| Method | Endpoint | Description |
|--------|----------|-------------|
| DELETE | `/report-closed/{cafe_id}?api-key={key}` | Deletes a cafe — requires a valid API key |

**Example:**
```
DELETE http://127.0.0.1:8080/report-closed/3?api-key=your_secret_key_here
```

**Sample Response:**
```json
{
  "response": {
    "success": "Successfully updated the price."
  }
}
```

**If wrong API key:**
```json
{
  "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
}
```

**If cafe not found:**
```json
{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
```

---

## 🔐 Authentication

The **DELETE** endpoint is protected. You must pass your secret API key (set in `.env`) as a query parameter:
```
?api-key=your_secret_key_here
```

---

## 📁 Project Structure

```
.
├── main.py            # Main Flask app
├── .env               # Environment variables (do not commit!)
├── .gitignore
├── instance/
│   └── cafes.db       # SQLite database (auto-created)
└── templates/
    └── index.html     # Homepage template
```

---

## 🚀 Quick Test (after running the server)

```bash
# Get a random cafe
curl http://127.0.0.1:8080/random

# Get all cafes
curl http://127.0.0.1:8080/all

# Search by location
curl "http://127.0.0.1:8080/search?loc=London"

# Add a cafe
curl -X POST http://127.0.0.1:8080/add \
  -F "name=My Cafe" -F "map_url=https://maps.google.com" \
  -F "img_url=https://example.com/img.jpg" -F "loc=London" \
  -F "sockets=True" -F "toilet=True" -F "wifi=True" \
  -F "calls=False" -F "seats=20-30" -F "coffee_price=£2.50"

# Update price
curl -X PATCH "http://127.0.0.1:8080/update-price/1?new_price=£3.00"

# Delete a cafe
curl -X DELETE "http://127.0.0.1:8080/report-closed/1?api-key=your_secret_key_here"
```
