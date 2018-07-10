# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

# This file contains the chromosone (solution) object

import random

# The Chromosone class

class Chromosone:
    '''The Chromosone class represents a chromosone (a solution)''' 

    def __init__(self, num_mediums):
        '''Creates a new random solution'''
        arr = []
        for i in range(num_mediums):
            arr.append(random.randint(0, 1))


        self.array = arr
        self.fitness = 0
        #print(arr)
    
    def setFitness(self, fit_val):
        '''Sets the fitness for the chromosone'''
        self.fitness = fit_val

