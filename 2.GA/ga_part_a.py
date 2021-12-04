import numpy
import pygad
import testfunctions.tests as tests
from inspect import getmembers, isfunction

# ---------------------------------------------------------------------------- #
#                This is a solution for part A of the assignment               #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                            Autho: Mh Samadi (Will)                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#          Look at the explanation of part A in the assignment picture         #
# ---------------------------------------------------------------------------- #

# get every test function in tests.py
functions = getmembers(tests, isfunction)
# to drop two functions of python modules
functions.pop()
functions.pop()

dims = [10, 30, 50]

# run the g algorithm 10 times for each test function in 3 different dimensionalities
func_idx = 0
for func_name, test_function in functions:
    print("running GA for {function_name}".format(num=func_idx, function_name=func_name))
    dim_idx = 0
    
    for dim in dims:
        print("{di}/3".format(di=dim_idx))
        dim_idx += 1

        avg_fitness = 0
        for i in range(10):
            ga_instance = pygad.GA(
                num_generations=10000,
                num_parents_mating=4,
                fitness_func=test_function,
                sol_per_pop=8,
                num_genes=dim,
                init_range_low=-100,
                init_range_high=100,
                parent_selection_type="sss",
                keep_parents=1,
                crossover_type="single_point",
                mutation_type="random",
                mutation_percent_genes=10,
                suppress_warnings=True
            )

            ga_instance.run()

            solution, solution_fitness, solution_idx = ga_instance.best_solution()
            avg_fitness += solution_fitness
            #print("Parameters of the best solution : {solution}".format(solution=solution))
            #print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
            prediction = numpy.sum(solution)
            #print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
            print('.', end='', flush=True)
        print("")
        avg_fitness /= 10
        print("avg fitness for dim={dim} : {fitness}".format(dim=dim, fitness=avg_fitness))
    
    func_idx += 1

# output:
# running GA for f1
# 0/3
# ..........
# avg fitness for dim=10 : -1.8050327239513463e-05
# 1/3
# ..........
# avg fitness for dim=30 : -0.1786007239213459
# 2/3
# ..........
# avg fitness for dim=50 : -1.1361683429841367
# running GA for f2
# 0/3
# ..........

# avg fitness for dim=10 : -0.006540734826187866
# 1/3
# ..........
# avg fitness for dim=30 : -1.6448756566029867
# 2/3
# ..........
# avg fitness for dim=50 : -499.58154076582

# running GA for f4
# 0/3
# ..........
# avg fitness for dim=10 : -0.008043532332038628
# 1/3
# ..........
# avg fitness for dim=30 : -0.2727623760805419
# 2/3
# ..........
# avg fitness for dim=50 : -0.5390320534239433

# running GA for f5
# 0/3
# ..........
# avg fitness for dim=10 : -194.3597976208004
# 1/3
# ..........
# avg fitness for dim=30 : -27.41639242730937
# 2/3
# ..........
# avg fitness for dim=50 : -2965.6954790949003

# running GA for f6
# 0/3
# ..........
# avg fitness for dim=10 : -2.2400062612675484e-05
# 1/3
# ..........
# avg fitness for dim=30 : -0.16263241017087152
# 2/3
# ..........
# avg fitness for dim=50 : -1.214601837848738

# running GA for f7
# 0/3
# ..........
# avg fitness for dim=10 : -1.749594035601877
# 1/3
# ..........
# avg fitness for dim=30 : -12.424057893838476
# 2/3
# ..........
# avg fitness for dim=50 : -27.46897663214118

# running GA for f8
# 0/3
# ..........
# avg fitness for dim=10 : 529.0559085662156
# 1/3
# ..........
# avg fitness for dim=30 : 1568.7105643507475
# 2/3
# ..........
# avg fitness for dim=50 : 2702.3751280459187

# running GA for rastrigin
# 0/3
# ..........
# avg fitness for dim=10 : 830237.8858628023
# 1/3
# ..........
# avg fitness for dim=30 : 1124941.8844515975
# 2/3
# ..........
# avg fitness for dim=50 : 1773646.2538011025

# running GA for schwefel
# 0/3
# ..........
# avg fitness for dim=10 : -0.00012249626205101545
# 1/3
# ..........
# avg fitness for dim=30 : -0.06977087760243669
# 2/3
# ..........
# avg fitness for dim=50 : -0.2859622073186022

# running GA for schwefelproblem
# 0/3
# ..........
# avg fitness for dim=10 : 519.0695202986863
# 1/3
# ..........
# avg fitness for dim=30 : 1616.1946261069702
# 2/3
# ..........
# avg fitness for dim=50 : 2737.8350117785367