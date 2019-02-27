import numpy
class Emulator():
    # Class takes discrete 2D input field i (nxn numpy array), and 2D aperture function in Fourier plane f
    def __init__(self, i, f):
        self.input_field = i
        self.fourier_aperture = f

    # Simulates transmission of light through a lens, returning field in rear focal plane
    def lens_transmission(input):
        return numpy.fft.fft2(input)

    # Determine field incident on Fourier plane
    self.fourier_field = lens_transmission(self.input_field)
    self.fourier_transmission = self.fourier_field * self.fourier_aperture
    self.output_field = lens_transmission(self.fourier_transmission)