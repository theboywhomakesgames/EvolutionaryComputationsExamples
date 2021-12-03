from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.shape_base import block
from f5 import *

dimensions = (50, 1)
elementRange = 30
sigmaChangeFactor = elementRange / 5
sigmaMin = 0.01

for runNumber in range(3):
    # make a random guess
    sigma = elementRange / 5
    guess = np.random.rand(*dimensions) * elementRange * 2
    guess -= elementRange
    last_f = f5(guess)
    guesses = []
    guesses.append([guess[0], guess[1], last_f])

    counter = 0
    replacement = 0

    print(sigma)

    for i in range(10000):
        # add a random value to the guess
        change = np.random.normal(0, sigma, dimensions)
        new_guess = guess + change
        np.clip(new_guess, -30, 30)
        # test the guess
        f = f5(new_guess)
        # decide if we should keep the new value
        if(last_f >= f):
            last_f = f
            guess = new_guess
            guesses.append([guess[0], guess[1], last_f])
            replacement += 1
        counter += 1

        if(counter % 10 == 0 and counter != 0):
            successRate = replacement / 10
            diff = successRate - 0.2
            sigma = max(sigmaMin, sigma + diff * sigmaChangeFactor)
            #print(str(sigma) + " : " + str(successRate))
            counter = 0
            replacement = 0


    print(last_f)
    print(len(guesses))

    # The following is for showing the results in 3D
    
    # # draw the main function
    # x = np.linspace(-30, 30, 30)
    # y = np.linspace(-30, 30, 30)

    # X, Y = np.meshgrid(x, y)
    # Z = f5([X, Y])

    # fig = plt.figure()
    # ax = plt.axes(projection='3d')

    # ax.contour3D(X, Y, Z, 50, cmap='plasma')

    # X1 = []
    # for g in guesses:
    #     X1.append(g[0])
    # Y1 = []
    # for g in guesses:
    #     Y1.append(g[1])
    # Z1 = []
    # for g in guesses:
    #     Z1.append(g[2])

    # ax.scatter3D(X1, Y1, Z1, cmap="cool")

    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')

    # plt.show(block=True)