import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape, size

# 1
def f5(X, idx = 0):
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

    sum = np.multiply(sum, -1)
    return sum

# 2
def schwefel(X, idx = 0):
    Z = []
    X = np.abs(X)
    Z = np.max(X, axis=0)
    Z = np.power(Z, 2)
    Z = np.multiply(Z, -1)
    return Z

# 3
def schwefelproblem(X, idx = 0):
    sqrt = np.sqrt(np.abs(X))
    sin = np.sin(sqrt)
    Z = []
    for i in range(len(X)):
        Z.append(sin[i] * X[i])
    Z = np.sum(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z

# 4
def rastrigin(X, idx = 0):
    pi2 = math.pi * 2
    Z = np.multiply(X, pi2)
    Z = np.cos(Z)
    Z = np.multiply(Z, 10)
    X2 = np.power(X, 2)
    Z = np.multiply(Z, X2)
    Z = np.add(Z, 10)
    Z = np.sum(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z

# 5
def f1(X, idx = 0):
    X2 = np.power(X, 2)
    Z = np.sum(X2, axis=0)
    Z = np.multiply(Z, -1)
    return Z

# 6
def f4(X, idx = 0):
    Z = np.abs(X)
    Z = np.max(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z

# 7
def f6(X, idx = 0):
    Z = np.add(X, 0.5)
    Z = np.power(Z, 2)
    Z = np.sum(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z

# 8
def f8(X, idx = 0):
    Z = np.abs(X)
    Z = np.sqrt(Z)
    Z = np.sin(Z)
    minusX = np.multiply(X, -1)
    Z = np.multiply(Z, minusX)
    Z = np.sum(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z
    
# 9
def f2(X, idx = 0):
    Xabs = np.abs(X)
    Z1 = np.sum(Xabs, axis=0)
    Z2 = np.prod(Xabs, axis=0)
    Z = np.add(Z1, Z2)
    Z = np.multiply(Z, -1)
    return Z

# 10
def f7(X, idx = 0):
    Z = np.power(X, 4)
    for i in range(len(Z)):
        Z[i] = np.multiply(Z[i], i)
    rand = np.random.rand(*shape(Z))
    Z = np.add(Z, rand)
    Z = np.sum(Z, axis=0)
    Z = np.multiply(Z, -1)
    return Z