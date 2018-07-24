# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

# This is the main file

# Import all of the project files
from chromosome import Chromosome
from advertisement import Advertisement

import random, time, matplotlib.pyplot as plt, numpy as np
# Project variables

pop_size = 100
mutation_rate = 0.005
budget = 2500000

# Project methods

def fitness(advertisements, chromosome):
    '''Calculates the fitness for a certain chromosome'''

    cost = 0.0000
    reach = 0.0000
    impact = 0.0000

    for i in range(len(advertisements)):
        if chromosome.array[i] == 1:
            cost = cost + advertisements[i].cost
            reach = reach + advertisements[i].reach
            impact = impact + advertisements[i].impact

    if cost <= budget and cost > 0:
        fitness = (1 - (cost / reach)) * (impact / (len(advertisements) * 10)) * (cost / budget) # NEED TO FACTOR IN BUDGET AS WELL
    else:
        fitness = 0
    
    #print(fitness)

    return fitness

def crossover(c1, c2):
    '''Takes as input 2 chromosomes and returns a new chromosome which is a mix of the first 2'''
    c_new = Chromosome(len(advertisements))
    for i in range(len(advertisements)):
        if i % 2 == 0:
            c_new.array[i] = c1.array[i]
        else:
            c_new.array[i] = c2.array[i]
    #print(c_new.array)
    return c_new

def naturalSelection(population):
    '''Pick a random chromosome based on its fitness'''

    # normalize fitness values
    sum = 0;
    for i in range(pop_size):
        sum = sum + population[i].fitness

    if sum == 0:
        return population[random.randint(0, pop_size - 1)]
        
    for i in range(pop_size):
        population[i].score = population[i].fitness / sum
        #print("{0} with fitness {1} and score {2}").format(population[i].array, population[i].fitness, population[i].score)

    index = 0

    # random number between 0.0 and 1.0
    r = random.random()

    # subtracts score values until you get a negative number
    while r > 0:
        r = r - population[index].score
        index = index + 1
    
    index = index - 1 # cancels out last index + 1

    #print("Chose: {0} with fitness {1} and score {2}").format(population[index].array, population[index].fitness, population[index].score)
    return population[index]

# Main Algorithm
population = []

advertisements = [
                    Advertisement("National TV (Canada)", 1000000, 40000000, 5), 
                    Advertisement("National TV (USA)", 1250000, 45000000, 5),
                    Advertisement("Local TV (Victoria)", 100000, 500000, 6), 
                    Advertisement("Local TV (Seattle)", 175000, 600000, 6),
                    Advertisement("Superbowl TV", 5000000, 110000000, 8),
                    Advertisement("Youtube Video Ad (Large)", 100000, 1000000, 3),
                    Advertisement("Youtube Video Ad (Medium)", 80000, 750000, 3),
                    Advertisement("Web Banner (Large)", 700000, 10000000, 2),
                    Advertisement("Web Banner (Medium)", 500000, 8000000, 2),
                    Advertisement("Radio", 600000, 15000000, 4),
                    Advertisement("Newspaper (Victoria)", 50000, 550000, 3),
                    Advertisement("Newspaper (Vancouver)", 75000, 600000, 3),
                    Advertisement("Highway Billboard", 2000, 2000000, 1),
                    Advertisement("Times Square Billboard", 4000000, 150000000, 6),
                    Advertisement("Sponsored Content", 40000, 20000000, 7),
                    Advertisement("Product Placement", 40000, 25000000, 6),
                    Advertisement("Swag", 7700, 10000, 10)
                ]

for i in range(pop_size):
    population.append(Chromosome(len(advertisements)))

# Main loop

start_time = time.time()
elapsed_time = 0

plt.xlabel('Time (seconds)')
plt.ylabel('Fitness')
plt.title('Chromosome Fitness Over Time')
plt.ylim(0, 0.40)
x = []
y = []

best_chromosome = []
best_chromosome_fitness = 0

avg_fitness = 0

while(elapsed_time < 30):
    # calculate fitness for all chromosomes
    for i in range(pop_size):
        fit_num = fitness(advertisements, population[i])
        #print(fit_num)
        population[i].fitness = fit_num
    
    # Calculating average and max population fitness
    sum = 0
    max = 0
    max_index = 0
    for i in range(pop_size):
        if population[i].fitness > max:
            max = population[i].fitness
            max_index = i
        sum = sum + population[i].fitness

    if population[max_index].fitness > best_chromosome_fitness:
        best_chromosome_fitness = population[max_index].fitness
        best_chromosome = population[max_index].array

    last_avg_fitness = avg_fitness

    avg_fitness = sum / float(pop_size)

    y.append(avg_fitness)

    print("Average population fitness is {0} with a max fitness of {1}").format(avg_fitness, max)

    if avg_fitness >= 0.29:
        elapsed_time = time.time() - start_time
        print("Elapsed Time: {0}").format(elapsed_time)
        print('BREAK')
        x.append(elapsed_time)
        break

    # obtain a new population
    new_pop = []
    
    for i in range(pop_size):
        mate1 = naturalSelection(population)
        mate2 = naturalSelection(population)
        new_chromosome = crossover(mate1, mate2)
        new_chromosome.mutate(mutation_rate)
        new_pop.append(new_chromosome)
    
    if len(new_pop) == pop_size:
        population = new_pop
    else:
        print("Error! New population size is not the same as the last one")

    #print(population[0].array)
    elapsed_time = time.time() - start_time
    print("Elapsed Time: {0}").format(elapsed_time)
    x.append(elapsed_time)

print("The chromosome with the highest fitness is {0} with a score of {1}").format(best_chromosome, best_chromosome_fitness)

total_cost = 0

print("Using the following advertisement options:")

for i in range(len(best_chromosome)):
    if best_chromosome[i] == 1:
        total_cost = total_cost + advertisements[i].cost
        print(advertisements[i].name)

print("Which uses ${0} out of ${1} budget").format(total_cost, budget)

plt.plot(x, y, 'ro')
plt.show()