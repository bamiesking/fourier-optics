# fourier-optics
A repository for scripts for exploring spacial filtering in 4f systems

## Emulator Class
The `emulator.Emulator` object takes 1 required argument and one optional argument:
* Path to an image representing the 2D intensity distribution in the input plane of the 4f system.
* Transfer function of the Fourier plane of the 4f system.

Its only publicly visible variable is the `images` dictionary, which contains the input, Fourier, and output plane images in the form of PIL `Image` objects, accessible via `images['i']`, `images['f']`, and `images['o']` respectively. Note that the Fourier image represents the field transmitted in the Fourier plane, and so will show the effect of any spacial filter. In order to show the field incident on the Fourier plane, the filter `filters.uniform(1)` can be used (see below for more on included filters).

The Fourier plane image is adjusted to couteract the reciprocal relation between real space and frequency space, and to centre the Fourier transform pattern which is otherwise located at the very corners of the image. The function `rotate_quarters` takes a PIL `Image` and returns the same image, with each quarter rotated by 180 degrees.

## Filter Functions

`filters.py` contains a number of functions which generate numpy arrays representing different spacial filters of interest, namely:
* `transparent_circle(r)` which returns a transparent circle of radius `r` aligned centrally with the image.
* `opaque_circle(r)` which returns the complement of the above.
* `cosine_window(r, n)` which returns the apodizing `n`th order cosine window function of radius `r`.
* `sine_window(r, n)` which returns the complement of the above.
* `grating(d, t)` which returns a coarse grating of vertical slits separated uniformly by `d` pixels, rotated through an angle `t` degrees.
