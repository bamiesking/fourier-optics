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


def grating(d, t):
    if t %((np.pi)/2) == 0:
        b = np.full((x, y), 0)
        for i in range(0, x, int(x / d)):
            b[:, i] = np.full((x), 1.0)
        return b
    elif t%(np.pi) == 0:
        b = np.full((x, y), 0)
        for i in range(0, y, int(y / d)):
            b[i,:] = np.ones((y),1.0)
        return b
    elif t%((np.pi/2)/2) != 0 and t%(np.pi) != 0:
        b = np.zeros((x,y))
        for i in range(0, x, int((x/d)*np.cos(t))):
            for j in range(0,y,int((y/d)*np.sin(t))):
                b[i,j] = 1.0
        return b
def ones():
    return np.full((x,y), 1.0)


if __name__ == '__main__':
    afilter = transparent_circle(100)
    plt.imshow(Image.fromarray(afilter*256))
    plt.show()

