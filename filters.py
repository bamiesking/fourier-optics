import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Set dimensions of array to be equal to pixels of CCD images
y, x = 1280, 1024


# Define small transparent circular filter
def transparent_circle(R):
    a = np.zeros((x, y))
    for i in range(0,x):
        for j in range(0,y):
            r = np.sqrt(np.abs(x/2 - i)**2 + np.abs(y/2 - j)**2)
            if r <= R:
                a[i, j] = 1
    print(a.max())
    return a


# Define small opaque circular filter as complement of small transparent circular filter
def opaque_circle(R):
    return np.full((x, y), 1) - transparent_circle(R)


if __name__ == '__main__':
    afilter = transparent_circle(100)
    plt.imshow(Image.fromarray(afilter*256))
    plt.show()

