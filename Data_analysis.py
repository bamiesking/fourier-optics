from PIL import Image
import numpy as np
from emulator import Emulator
import filters
import matplotlib.pyplot as plt
import scipy

#save two images - im1 is the image taken by the camera, im2 is the image processed by the computer
e = Emulator("21-02-19/FourDotsInput.tif", filters.ones())

im1 = Image.open("21-02-19/FourDotsInput.tif").convert(mode = 'L')

im2 = e.images['o']

pix1 = im1.load()
pix2 = im2.load()
def line_read(i,c, a):
    """i here is the line to be read and saved as an array
    c is the length of the line to be read
    a is the array being read"""
    b = np.zeros(c)
    for x in range(c):
        b[x] = a[i,x]
    return b
print (line_read(100, 1024, pix1))
