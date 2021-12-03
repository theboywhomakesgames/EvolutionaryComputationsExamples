import numpy as np
import matplotlib.pyplot as plt

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

def f5Helper(X, Y):
    result = []
    for i in range(0, len(X)):
        input = list(zip(X[i], Y[i]))
        result.append(f5(input))
    return result