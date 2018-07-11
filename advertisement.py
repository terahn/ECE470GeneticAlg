# ECE 470 Genetic Algorithm Project
# Terahn Harrison, Chris Ellard, Thor Reite

class Advertisement:
    '''The Advertisement class represents an advertising medium'''

    def __init__(self, name, cost, reach, impact):
        self.name = name
        self.cost = cost # in dollars
        self.reach = reach # in number of people
        self.impact = impact # an impact score between 1 and 10