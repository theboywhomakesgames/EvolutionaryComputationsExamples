from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block

# The following is for showing the results in 3D
def visualize(f, min, max, resolution, name="plt"):
    # draw the main function
    x = np.linspace(min, max, resolution)
    y = np.linspace(min, max, resolution)

    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.contour3D(X, Y, Z, 50, cmap='plasma')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.savefig("{name}.png".format(name=name))