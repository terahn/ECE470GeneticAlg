# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

# This is the main file

# Import all of the project files
from chromosone import Chromosone

import random
# Project variables

pop_size = 10
mutation_rate = 0.1
num_mediums = 10 # number of different advertising mediums that can be used
count = 10 # number of iterations of the loop

# Project methods

def fitness(chromosone):
    '''Calculates the fitness for a certain chromosone'''
    fitness = 1

    return fitness

def crossover(c1, c2):
    '''Takes as input 2 chromosones and returns a new chromosone which is a mix of the first 2'''
    c_new = Chromosone(num_mediums)
    for i in range(num_mediums):
        if i % 2 == 0:
            c_new.array[i] = c1.array[i]
        else:
            c_new.array[i] = c2.array[i]
    print(c_new.array)
    return c_new

def naturalSelection(population):
    '''Pick a random chromosone based on its fitness'''

    index = random.randint(0, pop_size - 1)

    return population[index]

# Main Algorithm
population = []

for i in range(pop_size):
    population.append(Chromosone(num_mediums))

# Main loop
while(count >= 0):
    # calculate fitness for all chromosones
    for i in range(pop_size):
        fit_num = fitness(population[i])
        #print(fit_num)
        population[i].setFitness(fit_num)
    
    #print(population[0].fitness)
    # obtain a new population
    new_pop = []
    
    for i in range(pop_size):
        mate1 = naturalSelection(population)
        mate2 = naturalSelection(population)
        new_pop.append(crossover(mate1, mate2))
    
    if len(new_pop) == pop_size:
        population = new_pop
    else:
        print("Error! New population size is not the same as the last one")

    #print(population[0].array)
    count = count - 1



