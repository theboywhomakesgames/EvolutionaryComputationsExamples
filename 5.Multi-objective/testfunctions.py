import numpy as np
import math

# ---------------------------------------------------------------------------- #
#                               Author MH.Samadi                               #
# ---------------------------------------------------------------------------- #

def kursawe1(X):
    X = np.array(X)
    expower = np.sqrt((X[0] ** 2) + (X[1] ** 2)) * -0.2
    sum = np.power(np.e, expower) * -10
    for i in range(1, len(X) - 1):
        expower = (X[i] ** 2) + (X[i + 1] ** 2) * -0.2
        sum += np.power(np.e, expower) * -10

    return sum

def kursawe2(X):
    X = np.array(X)
    sum = 0
    for i in range(len(X)):
        sum += np.power(np.abs(X[0]), 0.8) + 5 * np.sin(np.power(X[0], 3))

    return sum

def schaffer1(X):
    return X[0] ** 2

def schaffer2(X):
    return (X[0] - 2) ** 2

def zdtg(X):
    X = np.array(X)
    return 1 + 9 * np.sum(X[1:]) / (len(X) - 1)

def zdt1(X):
    return X[0]

def zdt2(X):
    g = zdtg(X)
    X = np.array(X)
    return g * (1 - math.sqrt(X[0]/g))

def zdt22(X):
    g = zdtg(X)
    X = np.array(X)
    return g * (1 - math.pow(X[0]/g, 2))

def zdt3g(X):
    X = np.array(X)
    return 1 + (9 / (len(X) - 1)) * np.sum(X[1:])

def zdt31(X):
    return X[0]

def zdt32(X):
    g = zdt3g(X)
    X = np.array(X)
    xg = X[0]/g
    return g * (1 - math.sqrt(xg) - xg * math.sin(10 * math.pi * X[0]))

def zdt4g(X):
    X = np.array(X)
    sum = 0
    for i in range(1, len(X)):
        sum += X[i] ** 2 - 10 * math.cos(4 * math.pi * X[i])
    return 91 + sum

def zdt41(X):
    return X[0]

def zdt42(X):
    g = zdt4g(X)
    X = np.array(X)
    return g * (1 - math.sqrt(X[0]/g))

def zdt6g(X):
    X = np.array(X)
    return 1 + 9 * math.pow(np.sum(X[1:]) / (len(X) - 1), 0.25)

def zdt61(X):
    return 1 - math.exp(-4 * X[0]) * math.pow(math.sin(6 * math.pi * X[0]), 6)

def zdt62(X):
    g = zdt4g(X)
    X = np.array(X)
    return g * (1 - math.pow(zdt61(X) / g, 2))