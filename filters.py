import numpy as np


# Set dimensions of array to be equal to pixels of CCD images
y, x = 1280, 1024


# Define small transparent circular filter
def transparent_circle(r):
    a = np.zeros((x, y))
    for i in range(0, x):
        for j in range(0, y):
            R = np.sqrt(np.abs(x/2 - i)**2 + np.abs(y/2 - j)**2)
            if R <= r:
                a[i, j] = 1
    print(a.max())
    return a


# Define small opaque circular filter as complement of small transparent circular filter
def opaque_circle(r):
    return np.full((x, y), 1) - transparent_circle(r)


def grating(d, t):
    if t % np.pi/2 == 0:
        b = np.full((x, y), 0.)
        for i in range(0, y, int(y / d)):
            b[:, i] = np.full(x, 1.0)
        return b
    elif t % np.pi == 0:
        b = np.full((x, y), 0.)
        for i in range(0, x, int(x / d)):
            b[i, :] = np.ones(y, 1.0)
        return b
    else:
        b = np.zeros((x, y))
        for i in range(0, x, int((x/d)*np.cos(t))):
            for j in range(0, y, int((y/d)*np.sin(t))):
                b[i, j] = 1.0
        return b


def ones():
    return np.full((x, y), 1.0)


