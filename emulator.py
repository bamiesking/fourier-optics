import numpy


class Emulator():
    # Class takes discrete 2D input field i (nxn numpy array), and 2D aperture function in Fourier plane f
    def __init__(self, i, f):
        self.input_field = i
        self.fourier_aperture = f

        # Determine field incident on Fourier plane
        #TODO: Split fourier transform output into quarters, rotate each by 180 deg, recombine to get corrected fourier field
        self.fourier_field = numpy.fft.fft2(self.input_field, norm='ortho')
        self.fourier_transmission = self.fourier_field * self.fourier_aperture
        self.output_field = numpy.fft.fftn(self.fourier_transmission, norm='ortho')
