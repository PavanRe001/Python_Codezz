# Dr. Semmelweis Handwashing Analysis

A data analysis project investigating Dr. Ignaz Semmelweis' 19th-century discovery that handwashing with chlorine drastically reduced deaths from childbed fever — using histograms, KDEs, and statistical testing to make the case visually.

## What This Covers

- Visualising distributions with histograms
- Superimposing histograms with differing data lengths
- Smoothing distributions using Kernel Density Estimates (KDE)
- Improving KDEs with boundary constraints
- Testing statistical significance with p-values using `scipy`
- Highlighting sections of a time series chart in Matplotlib
- Adding and configuring legends in Matplotlib
- Conditional element processing with NumPy's `.where()`

## Tech Stack

- **Language:** Python
- **Libraries:** pandas, NumPy, Matplotlib, scipy

## Setup

```bash
pip install pandas numpy matplotlib scipy
jupyter notebook
```

## The Story

Semmelweis correctly identified that doctors were transmitting "cadaverous particles" (bacteria) from autopsies to birthing mothers, causing childbed fever. His data proved it — but he presented it as dense tables, not visuals, and his abrasive approach earned him enemies rather than converts. His theory was rejected in his lifetime; he died in an asylum, ironically from sepsis. It took Louis Pasteur's germ theory, 20 years later, for his work to be vindicated.

This project revisits his data with modern visualisation tools to show what a difference a chart can make.
