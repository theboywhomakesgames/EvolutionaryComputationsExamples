import random
from numpy.lib.function_base import select
from pyeasyga import pyeasyga
import numpy as np
import numpy.random as npr
import datfileReader

# ---------------------------------------------------------------------------- #
#                                  QAP SOLVER                                  #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                               Author: MH Samadi                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                               Read the Problem                               #
# ---------------------------------------------------------------------------- #
width, distances, flows = datfileReader.read()

# ---------------------------------------------------------------------------- #
#                                Setup Algorithm                               #
# ---------------------------------------------------------------------------- #
seed_data = []
for i in range(width):
    seed_data.append(i + 1)
# ---------------------------------------------------------------------------- #
#                             Create A Random Gene                             #
# ---------------------------------------------------------------------------- #
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual


# ---------------------------------------------------------------------------- #
#                              Crossover Operation                             #
# ---------------------------------------------------------------------------- #
def create_child(parent_1, parent_2, crossover_index, crossover_range):
    child1 = np.ones(width, np.int8) * -1

    i = 0
    for p in parent_1[crossover_index:crossover_range + 1]:
        child1[crossover_index + i] = p
        i += 1

    for p2 in parent_2:
        if p2 not in child1:
            n = np.where(child1==-1)[0][0]
            child1[n] = p2
    
    return child1


def crossover(parent_1, parent_2):
    crossover_index = random.randrange(0, len(parent_1))
    co_range = random.randrange(crossover_index, len(parent_1))
    return create_child(parent_1, parent_2, crossover_index, co_range), create_child(parent_2, parent_1, crossover_index, co_range)


# ---------------------------------------------------------------------------- #
#                              Mutation Operation                              #
# ---------------------------------------------------------------------------- #
def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]


# ---------------------------------------------------------------------------- #
#                              Selection Operation                             #
# ---------------------------------------------------------------------------- #
def roulette_selection(population):
    max = sum([c for c in population])
    selection_probs = [c/max for c in population]
    return npr.choice(len(population), p=selection_probs)


# ---------------------------------------------------------------------------- #
#                               Fitness Function                               #
# ---------------------------------------------------------------------------- #
f_i = 0
def fitness (individual):
    global f_i
    sum = 0
    for i in range(width):
        for j in range(width):
            d = distances[i][j]
            f = flows[individual[i] - 1][individual[j] - 1]
            sum += d * f

    if(f_i % 10000 == 0):
        print(str(f_i/10000) + " : " + str(sum))
    f_i += 1
    return sum

# ---------------------------------------------------------------------------- #
#                                      Run                                     #
# ---------------------------------------------------------------------------- #
# create population
pop_size = 200

p_crossover = 0.9
p_mutation = 0.5

population = []
fitnesses = np.zeros(pop_size)

for j in range(pop_size):
    individual = create_individual(seed_data)
    population.append(individual)
    fitnesses[j] = fitness(individual)

# run it
for i in range(10000):
    # create offsprings
    # select two parents
    p1i = roulette_selection(fitnesses)
    flag = True
    p2i = -1
    while(flag):
        p2i = roulette_selection(fitnesses)
        if p1i is not p2i:
            flag = False

    # crossover
    c1 = population[p1i]
    c2 = population[p2i]
    if random.random() <= p_crossover:
        c1, c2 = crossover(c1, c2)

    # mutate
    if random.random() <= p_mutation:
        mutate(c1)
    if random.random() <= p_mutation:
        mutate(c2)
    
    f1 = fitness(c1)
    f2 = fitness(c2)
    
    maxidx = np.argmax(fitnesses)
    if f1 < fitnesses[maxidx]:
        fitnesses[maxidx] = f1
        population[maxidx] = c1
    
    maxidx = np.argmax(fitnesses)
    if f2 < fitnesses[maxidx]:
        fitnesses[maxidx] = f2
        population[maxidx] = c2

# print results
maxidx = np.argmax(fitnesses)
print(fitnesses[maxidx])
print(population[maxidx])

# ---------------------------------------------------------------------------- #
#                                    Results                                   #
# ---------------------------------------------------------------------------- #
# population results
# 200 - first run with pyeasyga - no steady state - 3946 - 10k iterations - ran for an hour
# 200 - second run with sss - 3808 - 10k iterations - ran for 10 seconds [ 4  1 10 15 13 21  7 19 20 22 14  6  9 23 17 11 16  8 25 12 24 18  3  2 5]

# 10 - 4036.0 -- [14 21 11  4  8 12 13 15 22  7  5 23 20  2  3 24  1 10 18 19 17  6 25 16  9]
# 25 - 4012.0 -- [16  1 20 15 12  5  6  3  9  8 17  4 24 11 21 13 23 19  7 14 10  2 22 18 25]
# 50 - 3898.0 -- [ 2  7 14  5 17 11 19 15 12  3 22 13  6  8  4  9 10 25  1 16 23 20 21 18 24]
# 100 - 3862.0 -- [ 5 15 20 13 12 21  1 19 23 17  2  9 10 16 25  3  8  6  7  4 18 11 22 14 24]
# 500 - 4204.0 -- [15 22 13  1 20 16  9  7 19 21 14  6 10 23 17 25  3 11  8 24  2  5 18  4 12]
# 1000 - 4446.0 -- [12  8 23 20 13 22  9 10  3 25 17 14 16  7 19  5  2  6 21 15 18  1 11  4 24]
# 2000 - 4592.0 -- [13 23 19 15  1 10  9 22  3 17  7 24 11 20 21  6 14  8  4 18  5  2 12 25 16]
# 3000 - 4674.0 -- [11  8 14 15 20 18  4  3 13 25 23 12 16  7  6 22  9  2  1 21 17 10  5 19 24]
# 5000 - 4774.0 -- [22  1  4 14 17 20 23  8  9 19  3  7 15 25 21  5  2 16  6 10 13 11 24 18 12]
# 5000 ran for 250k iterations! - 

# pc results
# 0.9 - 3794.0 -- [13  4 21 24 12 23  7 14  3 17 19 10  6 16 18  1  9  8 25 11 22 15 20  2  5]
# 0.8 - 3808.0 -- [ 4  1 10 15 13 21  7 19 20 22 14  6  9 23 17 11 16  8 25 12 24 18  3  2 5]
# 0.2 - 4538.9 -- [21 25 20 24  2 19 15 12  4 10  5 11 18 13 14  9  1  8 16  3  7  6 17 23 22]

# pm results
# 0.1 - 3960.0 -- [ 5 15 20 22  1  2 25  8  9 23 11  4  6 10 19 21 16  7 14  3 24 12 18 17 13]
# 0.2 - 3808.0 -- [ 4  1 10 15 13 21  7 19 20 22 14  6  9 23 17 11 16  8 25 12 24 18  3  2 5]
# 0.5 - 3892.0 -- [ 5  2 17 12  4 11 18  3 25 24  8  9 14 16 21  6 19 23  7 10 22  1 20 15 13]