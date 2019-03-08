import numpy as np
from PIL import Image


# Set dimensions of array to be equal to pixels of CCD images
y, x = 1280, 1024


# SPACIAL FREQUENCY FILTERS
def transparent_circle(r):
    """Returns a transparent circular aperture of radius r in pixels"""
    a = np.zeros((x, y))
    for i in range(0, x):
        for j in range(0, y):
            R = np.sqrt(np.abs(x/2 - i)**2 + np.abs(y/2 - j)**2)
            if R <= r:
                a[i, j] = 1
    return a


def opaque_circle(r):
    """Returns the complementary filter of transparent_circle: a small opaque circle of radius r pixels."""
    return np.full((x, y), 1) - transparent_circle(r)


# APODIZING FILTERS
def cosine_window(r, n=1):
    """Returns the nth-order cosine window of radius r in pixels."""
    a = np.zeros((x, y))
    for i in range(0, x):
        for j in range(0, y):
            R = np.sqrt(np.abs(x/2 - i)**2 + np.abs(y/2 - j)**2)
            if R <= r:
                a[i, j] = np.cos(np.pi/2 * R/r)**n
    return a


def sine_window(r, n=1):
    """Returns the nth-order sine window of radius r."""
    return np.full((x, y), 1) - cosine_window(r, n)


# COARSE GRATING
def grating(d, t):
    """Returns a vertical coarse grating with slit spacing d pixels, rotated an angle t from the horixontal"""
    array, n = np.zeros((3*x, 3*y)), 0
    while n*d < 3*y:
        array[:, n*d] = np.ones(3*x, float)
        n += 1

    canvas = Image.fromarray(array)
    return np.array(canvas.rotate(t).crop((y, x, 2*y, 2*x)))


# UNIFORM FILTER
def uniform(a):
    """Returns a uniform filter with transparency |a| in [0,1]. If |a|>1, uses |a|=1."""
    a = np.abs(a)
    return np.full((x, y), min(a, 1))

