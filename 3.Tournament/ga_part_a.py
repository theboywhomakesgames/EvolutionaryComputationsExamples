import numpy
import pygad
import testfunctions.tests as tests
from inspect import getmembers, isfunction

# ---------------------------------------------------------------------------- #
#                            Autho: Mh Samadi (Will)                           #
# ---------------------------------------------------------------------------- #

# get every test function in tests.py
functions = getmembers(tests, isfunction)

# to drop two functions of python modules
functions.pop()
functions.pop()

# ---------------------------------------------------------------------------- #
#                                  First Test                                  #
# ---------------------------------------------------------------------------- #
func_idx = 0
for func_name, test_function in functions:
    print("running GA for {function_name}".format(num=func_idx, function_name=func_name))
    avg_fitness = 0
    for i in range(10):
        ga_instance = pygad.GA(
            num_generations=10000,
            num_parents_mating=4,
            fitness_func=test_function,
            sol_per_pop=8,
            num_genes=10,
            init_range_low=-100,
            init_range_high=100,
            parent_selection_type="tournament",
            K_tournament=5,
            keep_parents=1,
            crossover_type="single_point",
            mutation_type="random",
            mutation_percent_genes=10,
            suppress_warnings=True
        )

        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        avg_fitness += solution_fitness
        prediction = numpy.sum(solution)
        print('.', end='', flush=True)

    print("")
    avg_fitness /= 10
    print("avg fitness for dim={dim} : {fitness}".format(dim=10, fitness=avg_fitness))
    print("")
    print("")
    
    func_idx += 1

# Results:
# running GA for f1
# ..........
# avg fitness for dim=10 : -0.23109982024469983


# running GA for f2
# ..........
# avg fitness for dim=10 : -1.1616965228809146


# running GA for f4
# ..........
# avg fitness for dim=10 : -0.37146264360503983


# running GA for f5
# ..........
# avg fitness for dim=10 : -69.93481847947275


# running GA for f6
# ..........
# avg fitness for dim=10 : -0.26544027468160314


# running GA for f7
# ..........
# avg fitness for dim=10 : -4.417646658544345


# running GA for f8
# ..........
# avg fitness for dim=10 : 505.29945178900687


# running GA for rastrigin
# ..........
# avg fitness for dim=10 : 730989.5018698667


# running GA for schwefel
# ..........
# avg fitness for dim=10 : -0.140055128599259


# running GA for schwefelproblem
# ..........
# avg fitness for dim=10 : 534.8804230934186

# ---------------------------------------------------------------------------- #
#                                  Second Test                                 #
# ---------------------------------------------------------------------------- #
func_idx = 0
for func_name, test_function in functions:
    print("running GA for {function_name}".format(num=func_idx, function_name=func_name))
    avg_fitness = 0
    for i in range(10):
        ga_instance = pygad.GA(
            num_generations=10000,
            num_parents_mating=4,
            fitness_func=test_function,
            sol_per_pop=8,
            num_genes=10,
            init_range_low=-100,
            init_range_high=100,
            parent_selection_type="rws",
            gene_type=[float, 64],
            K_tournament=5,
            keep_parents=1,
            crossover_type="single_point",
            mutation_type="random",
            mutation_percent_genes=10,
            suppress_warnings=True
        )

        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        avg_fitness += solution_fitness
        prediction = numpy.sum(solution)
        print('.', end='', flush=True)

    print("")
    avg_fitness /= 10
    print("avg fitness for dim={dim} : {fitness}".format(dim=10, fitness=avg_fitness))
    print("")
    print("")
    
    func_idx += 1

# Results:
# running GA for f1
# ..........
# avg fitness for dim=10 : -8.025826667413272


# running GA for f2
# ..........
# avg fitness for dim=10 : -31861159818346.387


# running GA for f4
# ..........
# avg fitness for dim=10 : -0.7003932685246362


# running GA for f5
# ..........
# avg fitness for dim=10 : -8170757.475103567


# running GA for f6
# ..........
# avg fitness for dim=10 : -6.269345005668728


# running GA for f7
# ..........
# avg fitness for dim=10 : -15009082.26153121


# running GA for f8
# ..........
# avg fitness for dim=10 : 379.829039509553


# running GA for rastrigin
# ..........
# avg fitness for dim=10 : 403254.39073486894


# running GA for schwefel
# ..........
# avg fitness for dim=10 : -12.909230882938663


# running GA for schwefelproblem
# ..........
# avg fitness for dim=10 : 265.26007153173845

# ---------------------------------------------------------------------------- #
#                                  Third Test                                  #
# ---------------------------------------------------------------------------- #
func_idx = 0
for func_name, test_function in functions:
    print("running GA for {function_name}".format(num=func_idx, function_name=func_name))
    avg_fitness = 0
    for i in range(10):
        ga_instance = pygad.GA(
            num_generations=10000,
            num_parents_mating=4,
            fitness_func=test_function,
            sol_per_pop=8,
            num_genes=10,
            init_range_low=-100,
            init_range_high=100,
            parent_selection_type="tournament",
            gene_type=[float, 64],
            K_tournament=5,
            keep_parents=1,
            crossover_type="single_point",
            mutation_type="random",
            mutation_percent_genes=10,
            suppress_warnings=True
        )

        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        avg_fitness += solution_fitness
        prediction = numpy.sum(solution)
        print('.', end='', flush=True)

    print("")
    avg_fitness /= 10
    print("avg fitness for dim={dim} : {fitness}".format(dim=10, fitness=avg_fitness))
    print("")
    print("")
    
    func_idx += 1

# Results:
# running GA for f1
# ..........
# avg fitness for dim=10 : -0.2405375626296306


# running GA for f2
# ..........
# avg fitness for dim=10 : -1.195533415049443


# running GA for f4
# ..........
# avg fitness for dim=10 : -0.4105388569182325


# running GA for f5
# ..........
# avg fitness for dim=10 : -164.66535184037326


# running GA for f6
# ..........
# avg fitness for dim=10 : -0.3182177155614436


# running GA for f7
# ..........
# avg fitness for dim=10 : -4.861745515863617


# running GA for f8
# ..........
# avg fitness for dim=10 : 582.707175435505


# running GA for rastrigin
# ..........
# avg fitness for dim=10 : 734965.7390727879


# running GA for schwefel
# ..........
# avg fitness for dim=10 : -0.1681049916782678


# running GA for schwefelproblem
# ..........
# avg fitness for dim=10 : 621.9048250154626
