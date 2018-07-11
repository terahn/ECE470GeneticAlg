# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

# This file contains the chromosome (solution) object

import random

# The chromosome class

class Chromosome:
    '''The chromosome class represents a chromosome (a solution)''' 

    def __init__(self, num_mediums):
        '''Creates a new random solution'''
        arr = []
        for i in range(num_mediums):
            arr.append(random.randint(0, 1))


        self.array = arr
        self.fitness = 0
        self.score = 0 # normalized fitness value for selection
        #print(arr)
    
    def setFitness(self, fit_val):
        '''Sets the fitness for the chromosome'''
        self.fitness = fit_val

    def setScore(self, score):
        '''Sets the score for the chromosome'''
        self.score = score

    def mutate(self, mutation_rate):
        
        '''Mutates the chromosome every so often according to the mutation rate'''
        for i in range(len(self.array)):
            if random.random() < mutation_rate:
                #print("MUTATE")
                if self.array[i] == 0:
                    self.array[i] = 1
                else:
                    self.array[i] = 0
