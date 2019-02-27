import numpy as np
from PIL import Image


class Emulator():
    """Initialised with a PIL Image describing the field in the input plane, and a numpy array describing the aperture function/pupil function in the Fourier plane.

    Produces PIL images representing field in Fourier plane and in output plane."""
    def __init__(self, i, f):
        input_image = Image.open(i).convert(mode='L')
        fourier_aperture = f

        # Determine field incident on Fourier plane
        fourier_field = np.fft.fft2(input_image, norm='ortho')
        fourier_transmission = fourier_field * fourier_aperture
        output_field = np.fft.fftn(fourier_transmission, norm='ortho')
        output_image = Image.fromarray(np.abs(output_field))

        #  Transform Fourier plane image to represent proper field
        fourier_image = Image.fromarray(np.abs(fourier_transmission))
        w, h = fourier_image.size
        quarters = [fourier_image.crop((0, 0, int(w/2), int(h/2))),
                    fourier_image.crop((int(w/2), 0, int(w),int(h/2))),
                    fourier_image.crop((0, int(h/2),int(w/2), int(h))),
                    fourier_image.crop((int(w/2), int(h/2), int(w), int(h)))]

        for i in range(0, 4):
            quarters[i] = quarters[i].rotate(180)

        fourier_image.paste(quarters[0], (0, 0, int(w/2), int(h/2)))
        fourier_image.paste(quarters[1], (int(w/2), 0, int(w), int(h/2)))
        fourier_image.paste(quarters[2], (0, int(h/2), int(w/2), int(h)))
        fourier_image.paste(quarters[3], (int(w/2), int(h/2), int(w),int(h)))

        # Create accessible array of images
        self.images = {'i': input_image, 'f': fourier_image, 'o': output_image}
