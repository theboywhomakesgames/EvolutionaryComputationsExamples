import numpy
import pygad

import testfunctions.tests as tests
import visualizer.vis as vis

# ---------------------------------------------------------------------------- #
#                    this code visualizes the test functions                   #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                           Author : Mh Samadi (Will)                          #
# ---------------------------------------------------------------------------- #

# Visualize the test functions in 2D
vis.visualize(tests.f1, -30, 30, 300, "f1")
vis.visualize(tests.f2, -30, 30, 300, "f2")
vis.visualize(tests.f4, -30, 30, 300, "f4")
vis.visualize(tests.f5, -30, 30, 300, "f5")
vis.visualize(tests.f6, -30, 30, 300, "f6")
vis.visualize(tests.f7, -30, 30, 300, "f7")
vis.visualize(tests.f8, -30, 30, 300, "f8")
vis.visualize(tests.schwefel, -2, 2, 100, "schwefel")
vis.visualize(tests.schwefelproblem, -500, 500, 500, "shcwefelproblem")
vis.visualize(tests.rastrigin, -3, 3, 200, "rastrigin")