# Google Play Store Data Analysis 📱📊

An end-to-end data exploration project from Day 76 of **[100 Days of Code™: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**. This project focuses on cleaning, manipulating, and visualizing a scraped dataset of Android apps using **Pandas** and advanced **Plotly** interactive charts to uncover market dynamics.

---

## 🗺️ Learning Roadmap & Core Concepts

### 1. Data Cleaning & Initial Exploration
* **Handling Missing Values:** Discovered and removed incomplete records (`NaN` values) in critical columns like `Rating` using `.dropna()`.
* **Removing Duplicates:** Identified and eliminated redundant app listings with `.duplicated()` and `.drop_duplicates()` to ensure data integrity.
* **Random Sampling:** Inspected data integrity and structure across random distributions using `.sample()`.

### 2. Numeric Type Conversions & Preprocessing
* **The Problem:** Columns like `Installs` and `Price` were imported as text/object data types due to formatting characters (e.g., `1,000,000+`, `$4.99`).
* **The Fix:** 1. Standardized rows into text strings using `.astype(str)`.
  2. Stripped out formatting clutter (commas, plus signs, currency symbols) using `.str.replace()`.
  3. Converted the clean text numbers into actual math-ready values using `pd.to_numeric()`.

### 3. Structural Data Transformation (Nested Categories)
* **Unnesting Text:** Dealt with apps assigned to multiple categories inside the `Genres` column (e.g., `Strategy;Action`) by separating elements using `.str.split(';', expand=True)`.
* **Flattening Rows:** Combined the newly generated columns vertically into a single, continuous series using `.stack()`, uncovering the true breakdown of unique app store genres via `.value_counts()`.

### 4. Advanced Visualization & Mathematical Scaling
* **Pie & Donut Charts:** Segmented categorical market share distribution across content ratings and genres.
* **Logarithmic Scaling (`yaxis=dict(type='log')`):** Used an exponential power-of-10 scale on bar charts and scatter plots. This prevented hyper-viral apps (1B+ downloads) from drowning out lower-tier apps, bringing both massive and small metrics into a readable visual framework.
* **Box Plot Anatomy:** * Analyzed market risk by comparing **Medians** (middle lines) and the **Interquartile Range** (box size).
  * Evaluated how app categories represent a "lottery economy"—where median apps often lose money, but developers compete to hit the high-floating **Outlier** dots.

---

## 🛠️ Tech Stack & Tools Used
* **Language:** Python 3
* **Environment:** Jupyter Notebook / Google Colab
* **Libraries:** Pandas, NumPy, Plotly Express