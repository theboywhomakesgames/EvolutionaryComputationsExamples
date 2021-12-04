import cv2
import numpy as np
import pygad
import math
import gari

resolution = 128

image = cv2.imread('./resources/sample_image.jpg')
image = cv2.resize(image, (resolution, resolution))
target_chromosome = gari.img2chromosome(image)

save_step = 1000
step = 0
def fitness_fun(solution, solution_idx):
    global step

    fitness = np.sum(np.abs(target_chromosome-solution))
    # Negating the fitness value to make it increasing rather than decreasing.
    fitness = np.sum(target_chromosome) - fitness
    if(step % save_step == 0):
        img = gari.chromosome2img(solution, image.shape)
        cv2.imwrite('./output/{gen}.jpg'.format(gen=step), img)
        print(fitness)

    step += 1
    return fitness

ga_instance = pygad.GA(
    num_generations=20000,
    num_parents_mating=10,
    fitness_func=fitness_fun,
    sol_per_pop=20,
    num_genes=image.size,
    init_range_low=0.0,
    init_range_high=255.0,
    mutation_percent_genes=0.01,
    mutation_type="random",
    mutation_by_replacement=True,
    random_mutation_min_val=0.0,
    random_mutation_max_val=255.0
)

ga_instance.run()