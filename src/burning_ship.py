from numba import jit
import numpy as np


@jit
def burning_ship(real, imaginary, max_iter):
    c = complex(real, imaginary)
    z = 0.0j

    for i in range(max_iter):
        z = (np.abs(z.real) + np.abs(z.imag)*1j) ** 2 + c

        if z.real ** 2 + z.imag ** 2 > 4:
            return i

    return 0
