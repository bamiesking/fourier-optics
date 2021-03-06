from PIL import Image
import numpy as np
from emulator import Emulator
import matplotlib.pyplot as plt
"""import scipy.optimize
import scipy.stats
import scipy.ticker as ticker"""


#save two images - im1 is the image taken by the camera, im2 is the image processed by the computer
e = Emulator("21-02-19/FourDotsInput.tif")

im1 = Image.open("21-02-19/FourDotsInput.tif").convert(mode='L')

im2 = e.images['o']
#read data and output it in a useful format


def line_read(a):
    """saves a PIL image as a numpy array, and outputs one line of interest specified by the maximum value of the array.
    a is the PIL image to be read"""
    b = np.array(a)
    d = np.unravel_index(b.argmax(), b.shape)

    return b[int(d[0])]


def shift_image(a, b):
    """Shifts the image ato match another, with respect to its maxima
    a is the basis image (the picture taken)
    b is the compared picture (Fourier transform)
    """
    a_arr = np.array(a)
    b_arr = np.array(b)
    b_roll = np.roll(b_arr, a_arr.argmax() - b_arr.argmax())
    return b_roll


im2_roll = shift_image(im1, im2)


def residuals(a, b):
    """this function takes in two arrays: a, the observed image and b, the theoretical prediction.
    It returns an array of the residuals
    """
    return b-a


data = {'measured': line_read(im1), 'theoretical': line_read(im2_roll)}

fig, axes = plt.subplots(2)

axes[0].plot(data['measured'], label='Measured')
axes[0].plot(data['theoretical'], label='Theoretical')
axes[0].legend()

axes[1].plot(residuals(data['measured'], data['theoretical']))
plt.show()
