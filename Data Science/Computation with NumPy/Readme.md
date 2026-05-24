# Day 77: Computation with NumPy and N-Dimensional Arrays

This repository contains my notes, challenges, and code snippets from Day 77 of the *100 Days of Code: The Complete Python Pro Bootcamp*. This module covers the core fundamentals of numerical computing in Python using NumPy, handling N-dimensional arrays ($ndarrays$), and manipulating image data.

---

## Lesson Summaries & Code Contents

| **NumPy Fundamentals**<br>• Core power of the N-Dimensional Array (`ndarray`).<br>• Analysing the shape (`.shape`) and dimensions (`.ndim`) of vectors and matrices. | **Array Creation & Inspections**<br>• Manual creation via `np.array()`<br>• Inspection of a 3D tensor (`mystery_array`) with shape `(3, 2, 4)`. |
| **Array Generation & Sequences**<br>• Generating structured numerical patterns and ranges automatically.<br>• Distributing values uniformly across a mathematical interval. | **Sequence Generation Challenges**<br>• `np.arange(10, 30)` to generate a vector from 10 to 29.<br>• `np.linspace(0, 100, 9)` to build an evenly spaced array. |
| **Slicing & Subsetting**<br>• Navigating complex structures using multi-axis slice coordinates.<br>• Reversing matrices and step-skipping sequence indices. | **Slicing Manipulations**<br>• Index filtering (`a[-4:-1:-1]`, `a[12:]`).<br>• Reversing arrays with step-inversion (`a[::-1]`).<br>• Extracting inner matrices (`mystery_array[:,:,0]`). |
| **Randomization & Visual Mapping**<br>• Generating synthetic multidimensional tensor data.<br>• Plotting linear math coordinates and visual representations. | **Matplotlib Plots**<br>• Multi-dimensional random data using `np.random.default_rng()`.<br>• Plotting coordinates on a graph.<br>• Displaying random matrix blocks via `plt.imshow()`. |
| **Linear Algebra & Matrix Math**<br>• Vector operations vs standard Python lists.<br>• Array broadcasting rules.<br>• Matrix dot products. | **Matrix Computations**<br>• Scalar broadcasting arithmetic.<br>• High-performance dot product multiplication using `@` and `np.matmul()`. |
| **Image Manipulation via Tensors**<br>• Representing digital images as data arrays.<br>• Modifying pixel data channels via vector math.<br>• Correcting legacy environment bugs. | **Image Processing Challenges**<br>• Handling Scipy's `face()` image dataset migration using `pooch`.<br>• Grayscale conversions using custom dot-product matrix weights: `[0.2126, 0.7152, 0.0722]`.<br>• Flipping structural elements upside down (`img[::-1]`). |

---

## Environment Setup & Fixes

### ⚠️ Scipy Deprecation Warning
Older lecture notebooks import the sample raccoon dataset using `from scipy import misc; img = misc.face()`. In modern environments, this throws an `AttributeError`.

**Fix:** Install `pooch` and use the updated `scipy.datasets` library module:
```python
!pip install pooch
import scipy.datasets as datasets
import matplotlib.pyplot as plt

img = datasets.face()
plt.imshow(img)