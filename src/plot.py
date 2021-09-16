import numpy as np
import matplotlib.pyplot as plt
from numba import jit

from mandelbrot import mandelbrot
from burning_ship import burning_ship

WIDTH = 1200
HEIGHT = 800

# best get_grid constants for different fractals (as ive found from experimenting): 

# mandelbrot 
# xstart, xstop = -2, 1
# ystart, ystop = 1, 1

# burning_ship
xstart, xstop = -2, 1.5
ystart, ystop = -2, 1

@jit
def get_grid():
    grid = np.zeros((WIDTH, HEIGHT))
    for real_index, real in enumerate(np.linspace(xstart, xstop, WIDTH)): 
        for imaginary_index, imaginary in enumerate(np.linspace(ystart, ystop, HEIGHT)):
            grid[real_index, imaginary_index] = burning_ship(real, imaginary, 80) # change to whatever fractal

    return grid


def draw():
    grid = get_grid()
    plt.figure(dpi = 100)
    plt.imshow(grid.T, cmap = 'hot', interpolation = 'bilinear', extent = [-2, 1, -1, 1])
    plt.axis('off')
    # plt.savefig('outputs/mandel2.png', dpi = 100, transparent=True)
    plt.show()


if __name__ == '__main__':
    draw()