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



pix1_arr = line_read(im1)
pix2_arr = line_read(im2)

plt.plot(pix1_arr, label = 'real image')
plt.plot(pix2_arr, label = 'theoretical prediction')
plt.legend()
plt.show()