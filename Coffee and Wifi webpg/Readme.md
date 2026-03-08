# ☕ Bangalore Cafe Finder

A curated web app to discover the best cafes in Bangalore — filtered by coffee quality, Wi-Fi strength, and power outlet availability. Perfect for remote workers, students, and coffee lovers.

---

## 🗺️ What It Does

- Browse a handpicked list of top cafes across Bangalore
- See each cafe's **opening & closing hours**
- Check ratings for **Coffee quality** ☕, **Wi-Fi strength** 💪, and **Power outlets** 🔌
- Click directly to open the cafe location in **Google Maps**

---

## 🏙️ Cafes Covered

Cafes span popular Bangalore neighbourhoods including:

`Indiranagar` · `Koramangala` · `Jayanagar` · `Whitefield` · `Church Street` · `Richmond Road` · `Basavanagudi` · `HSR Layout` · `Sadashivanagar`

---

## 📁 Project Structure

```
├── index.html         # Main UI
├── cafe-data.csv      # Cafe data (name, map link, hours, ratings)
└── README.md
```

---

## 📊 Data Format (`cafe-data.csv`)

| Column | Description |
|---|---|
| `Cafe Name` | Name of the cafe |
| `Location` | Google Maps link |
| `Open` | Opening time |
| `Close` | Closing time |
| `Coffee` | Coffee quality (☕ rating) |
| `Wifi` | Wi-Fi strength (💪 rating) |
| `Power` | Power outlet availability (🔌 rating) |

---

## ➕ Secret: Add a Cafe

> 🤫 Want to add a cafe to the list?

Navigate to `/add` on the site to access the hidden submission page where you can suggest a new cafe to be featured.

```
https://<your-site-url>/add
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git

# Open in browser
open index.html
```

No dependencies. No build step. Just open and go.

---

## 🤝 Contributing

1. Fork the repo
2. Add your cafe to `cafe-data.csv` following the existing format
3. Or use the secret `/add` page
4. Submit a pull request

---

## 📜 License

MIT — free to use, fork, and brew with. ☕
