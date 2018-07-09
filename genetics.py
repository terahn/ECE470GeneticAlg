# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

# This is the main file

# Import all of the project files
from chromosone import Chromosone

# Project variables

pop_size = 100
mutation_rate = 0.1
num_mediums = 10

# Main Algorithm
population = []

for i in range(pop_size):
    population.append(Chromosone(10))

print(len(population))