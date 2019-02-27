import numpy as np
from PIL import Image


class Emulator():
    """Initialised with a PIL Image describing the field in the input plane, and a numpy array describing the aperture function/pupil function in the Fourier plane.

    Produces PIL images representing field in Fourier plane and in output plane."""
    def __init__(self, i, f):
        self.input_image = Image.open(i).convert(mode='L')
        self.fourier_aperture = f

        # Determine field incident on Fourier plane
        self.fourier_field = np.fft.fft2(self.input_image, norm='ortho')
        self.fourier_transmission = self.fourier_field * self.fourier_aperture
        self.output_field = np.fft.fftn(self.fourier_transmission, norm='ortho')
        self.output_image = Image.fromarray(np.abs(self.output_field))

        #  Transform Fourier plane image to represent proper field
        fourier_image_before = Image.fromarray(np.abs(self.fourier_transmission))
        quarters = [fourier_image_before.crop(
            (0, 0, int(fourier_image_before.width / 2), int(fourier_image_before.height / 2))),
                    fourier_image_before.crop((int(fourier_image_before.width / 2), 0, int(fourier_image_before.width),
                                               int(fourier_image_before.height / 2))),
                    fourier_image_before.crop((0, int(fourier_image_before.height / 2),
                                               int(fourier_image_before.width / 2), int(fourier_image_before.height))),
                    fourier_image_before.crop((
                                              int(fourier_image_before.width / 2), int(fourier_image_before.height / 2),
                                              int(fourier_image_before.width), int(fourier_image_before.height)))]

        for i in range(0, 4):
            quarters[i] = quarters[i].rotate(180)

        fourier_image_before.paste(quarters[0],
                                   (0, 0, int(fourier_image_before.width / 2), int(fourier_image_before.height / 2)))
        fourier_image_before.paste(quarters[1], (
        int(fourier_image_before.width / 2), 0, int(fourier_image_before.width), int(fourier_image_before.height / 2)))
        fourier_image_before.paste(quarters[2], (
        0, int(fourier_image_before.height / 2), int(fourier_image_before.width / 2), int(fourier_image_before.height)))
        fourier_image_before.paste(quarters[3], (
        int(fourier_image_before.width / 2), int(fourier_image_before.height / 2), int(fourier_image_before.width),
        int(fourier_image_before.height)))
        self.fourier_image = fourier_image_before
