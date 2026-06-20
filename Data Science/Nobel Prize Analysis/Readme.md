Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn
A comprehensive data exploration and visualization project utilizing historical Nobel Prize records. This project focuses on uncovering geographic distributions, demographic patterns, institutional research shifts, and age trends among laureates by leveraging advanced data science tools in Python.

🚀 Key Learning Points & Features

Data Cleaning & Exploration
Missing Value Investigation: Discovered and handled NaN values across datasets.

Type Conversion: Converted object and string data types into appropriate numerical values for computational analysis.

Statistical Agility: Leveraged advanced Pandas functions including .value_counts(), .groupby(), .merge(), .sort_values(), and .agg().

Advanced Visualizations
Interactive Plotly Charts: Built customized donut and segmented bar charts to track prize categories and female laureate distributions.

Time-Series Smoothing: Implemented rolling averages to iron out short-term fluctuations and capture macro-level historical trends.

Geospatial Mapping: Designed an interactive Choropleth Map to display geographic prize distributions by country globally.

Regional Breakdowns: Generated multi-layered Sunburst Charts with Plotly to map out a granular view of where breakthrough research takes place.

Seaborn Regression & Distributions: Used sns.lmplot() with row, hue, and lowess smoothing parameters to visualize changing age trends across multiple categories.

Descriptive Statistics: Highlighted underlying patterns and distributions via Seaborn histograms, contrasting them with box plots to analyze data from different analytical lenses.

🛠️ Tech Stack
Language: Python 3

Environment: Google Colab / Jupyter Notebook

Core Libraries: Pandas, NumPy, Matplotlib, Seaborn, Plotly