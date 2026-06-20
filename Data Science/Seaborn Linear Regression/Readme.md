Linear Regression and Data Visualisation with Seaborn

This repository contains my projects, notes, and code implementations for Day 78 of the *100 Days of Code: The Complete Python Pro Bootcamp*. Today's focus bridges the gap between data exploration, advanced visualization techniques, and predictive statistical modeling.

---

## Lesson Summaries & Notebook Contents

| :--- | :--- |
| **Data Cleaning & Nested Loops**<br>• Removing unwanted characters (like currency symbols or commas) globally across datasets.<br>• Efficiently sanitizing multiple columns using nested iteration loops. | **Data Exploration & Isolation**<br>• Investigating film datasets with zero revenue entries.<br>• Filtering data on multiple nested conditions using both `.loc[]` and `.query()`. |
| **Advanced Visualizations & Styling**<br>• Constructing multi-dimensional bubble charts to display budget vs. revenue.<br>• Modifying plot clarity and styling using Seaborn themes combined with underlying Matplotlib parameters. | **Bubble Chart & Decade Mapping**<br>• Configuring `scatter_kws={'alpha': 0.4}` to cleanly track point density and overlapping plots.<br>• Implementing floor division (integer division `//`) to group releases into clean decade blocks. |
| **Superimposing Regression Models**<br>• Overlaying straight best-fit trendlines directly onto visual scatter plots.<br>• Evaluating the mathematical fit of a model visually against real-world sample distributions. | **Seaborn Linear Regressions**<br>• Utilizing `sns.regplot()` and `sns.lmplot()` to plot linear trends.<br>• Analyzing data groups divided by historical eras or domestic vs. international releases. |
| **Scikit-Learn Machine Learning**<br>• Moving from pure visualization to algorithmic machine learning computations.<br>• Isolating features ($X$) and targets ($y$) to calculate the underlying formula coefficients. | **Scikit-Learn Regression Modelling**<br>• Initializing and fitting a `LinearRegression()` object.<br>• Calculating structural coefficients ($\theta_1$ slope and $\theta_0$ intercept).<br>• Evaluating predictive quality using the $R\text{-Squared}$ metric. |

---

## Technical Concept Review

### Linear Regression Formula
The machine learning model fits the dataset to a classic linear equation:

$$y = \theta_0 + \theta_1 X$$

* **$y$:** Target variable (e.g., Worldwide Revenue)
* **$X$:** Feature variable (e.g., Production Budget)
* **$\theta_0$:** The Intercept (base value if feature is 0)
* **$\theta_1$:** The Slope (expected change in $y$ per unit increase in $X$)

### Performance Metric ($R\text{-Squared}$)
The goodness-of-fit is assessed using the $R^2$ metric via `regression.score(X, y)`. This outputs a percentage showing how much variance in the target is successfully explained by the chosen feature model.