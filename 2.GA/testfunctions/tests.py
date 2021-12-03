import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

def f5(X):
    sum = 100 *np.power(
        X[1] - np.power(X[0], 2),
        2
    )
    + np.power(np.sum(X[0], -1), 2)

    len_ = len(X)

    for i in range(0, len_ - 1):
        sum += 100 *np.power(
            X[i + 1] - np.power(X[i], 2),
            2
        )
        + np.power(np.sum(X[i], -1), 2)

    return sum

def schwefel(X):
    Z = []
    X = np.abs(X)
    Z = np.max(X, axis=0)
    Z = np.power(Z, 2)
    return Z

def schwefelproblem(X):
    sqrt = np.sqrt(np.abs(X))
    sin = np.sin(sqrt)
    Z = []
    for i in range(len(X)):
        Z.append(sin[i] * X[i])
    Z = np.sum(Z, axis=0)
    return Z