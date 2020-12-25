import numpy as np
import matplotlib.pyplot as plt
from numba import jit

WIDTH = HEIGHT = 1000


@jit
def mandelbrot(real, imaginary, max_iter):
    c = complex(real, imaginary)
    z = 0.0j

    for i in range(max_iter):
        z = z ** 2 + c
        if z.real ** 2 + z.imag ** 2 >= 4:
            return i
    return max_iter


def get_grid():
    grid = np.zeros([WIDTH, HEIGHT])
    for real_index, real in enumerate(np.linspace(-2, 1, WIDTH)):
        for imaginary_index, imaginary in enumerate(np.linspace(1, -1, HEIGHT)):
            grid[real_index, imaginary_index] = mandelbrot(real, imaginary, 80)

    return grid


def draw():
    grid = get_grid()
    plt.figure(dpi = 100)
    plt.imshow(grid.T, cmap = 'hot', interpolation = 'bilinear', extent = [-2, 1, -1, 1])
    plt.axis('off')
    # plt.savefig('output.png', dpi = 'figure', transparent=True)
    plt.show()


if __name__ == '__main__':
    draw()