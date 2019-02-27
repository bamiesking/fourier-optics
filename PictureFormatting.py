import numpy
from PIL import Image

def PicArray(make_array, x, name):
    """This function has two options:
    If the bool make_array is set to True, then this function will output an array from the filename
    of the image, x. In this case, name is a dummy variable.
    If bool is set to False, then this function will output an image from an RGB value array, as given in the variable x. The variable
    name is the filename the image will be saved as"""
    if make_array = True:
        array = numpy.asarray(Image.open('x'))
        return array
    elif make_array = False:
        im = Image.fromarray(numpy.uint8(x))
        im.save(name)
        im.show()


def takePic(filename):
    image = Image.open(filename)
    return image


