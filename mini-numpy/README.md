# Mini NumPy — Python Array & Matrix Project

An educational implementation of selected NumPy-style features using nested Python lists and an `Array` class. The project explores numerical computing, linear algebra, and elementary RGB image transformations.

## Implemented features

- 1D, 2D and 3D array shape, dimension, size, flattening and reshaping
- 2D transpose; zeros, ones, identity matrices; arrange and linspace
- Element-wise addition, subtraction, multiplication, division and square
- Exponential, logarithm, square root, absolute value
- Sum, mean, min/max, argmin/argmax and Euclidean norm
- Dot product and matrix multiplication, determinants and inverse matrices
- Image loading, scaling, rotation, translation, brightness/red channel adjustment, contrast and grayscale operations via Pillow

The script includes comparisons with NumPy for a selection of functions.

## Requirements

```bash
pip install numpy pillow
```

## Run

```bash
python python_project.py
```

**Image demo setup:** The bottom of `python_project.py` currently references the author's original Windows image path (`image_path`). Replace it with a path to your own local RGB image before running the image-transformation tests. The sample image is not included in this repository.

## Notes

This is a learning project, **not a drop-in replacement for NumPy**. The current implementation has limitations for empty, irregular or mismatched arrays and several operations require particular dimensions. Consult the methods and example tests in the source for supported cases. The image routines use simple coordinate mapping and can leave unfilled pixels.

[Back to portfolio](../index.html#software)
