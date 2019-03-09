from PIL import Image
import numpy as np
from emulator import Emulator
import filters
import matplotlib.pyplot as plt
"""import scipy.optimize
import scipy.stats
import scipy.ticker as ticker"""


#save two images - im1 is the image taken by the camera, im2 is the image processed by the computer
e = Emulator("21-02-19/FourDotsInput.tif", filters.uniform(1))

im1 = Image.open("21-02-19/FourDotsInput.tif").convert(mode = 'L')

im2 = e.images['o']
#read data and output it in a useful format



def line_read(a):
    """saves a PIL image as a numpy array, and outputs one line of interest specified by the maximum value of the array.
    a is the PIL image to be read"""
    b = np.array(a)
    d = np.unravel_index(b.argmax(), b.shape)


    return b[int(d[0])]

def residuals(a, b):
    """this function takes in two arrays: a, the observed image and b, the theoretical prediction.
    It returns an array of the residuals
    """
    return b-a



pix1_arr = line_read(im1)
pix2_arr = line_read(im2)
fig, axes = plt.subplots(2)

axes[0].plot(pix1_arr, label = 'real image')
axes[0].plot(pix2_arr, label = 'theoretical prediction')
axes[1].plot(residuals(pix1_arr, pix2_arr))
plt.legend()
plt.show()