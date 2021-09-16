from numba import jit
import numpy as np


@jit
def mandelbrot(real, imaginary, max_iter):
    c = complex(real, imaginary)
    z = 0.0j

    for i in range(max_iter):
        z = z ** 2 + c

        if z.real ** 2 + z.imag ** 2 > 4:
            return i

    return max_iter #  not 0 because it looks cooler
