import numpy
import pygad
import math
import testfunctions.tests as tests
from inspect import getmembers, isfunction

# ---------------------------------------------------------------------------- #
#           This is for the last part of the part A of the assignment          #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                            Autho: Mh Samadi (Will)                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#           This part runs a GA algorithm to find the best parameters          #
#            for another GA algorithm which is trying to maximize an           #
#                        5D upside down f5 test function                       #
# ---------------------------------------------------------------------------- #

round = 0
def test_function(params, idx):
    global round
    print(str(round) + "/7014")
    round += 1
    # translating params
    pop = params[0]
    pop = max(1, pop)
    pop = int(pop)
    par = min(pop, 4)
    crossover_prob = params[1]/20
    crossover_prob = numpy.clip(crossover_prob, 0, 1)
    mutation_prob = params[2]/20
    mutation_prob = numpy.clip(mutation_prob, 0, 1)

    # running the GA for 5D flipped f5
    ga_instance = pygad.GA(
        num_generations=500,
        num_parents_mating=par,
        fitness_func=tests.f5,
        sol_per_pop=pop,
        num_genes=5,
        init_range_low=-30,
        init_range_high=30,
        parent_selection_type="sss",
        keep_parents=1,
        crossover_type="single_point",
        crossover_probability=crossover_prob,
        mutation_type="random",
        mutation_probability=mutation_prob,
        mutation_percent_genes=10,
        suppress_warnings=True
    )
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print(solution_fitness)
    print(params)
    print("==============")
    return solution_fitness

ga_instance = pygad.GA(
    num_generations=1000,
    num_parents_mating=4,
    fitness_func=test_function,
    sol_per_pop=8,
    num_genes=3,
    init_range_low=0,
    init_range_high=20,
    parent_selection_type="sss",
    keep_parents=1,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10,
    suppress_warnings=True
)
ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(solution)
print(solution_fitness)

# [16.80311391 15.02916105  6.84050387]
# -1.8389852656472134e-05