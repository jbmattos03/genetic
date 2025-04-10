"""
This module defines the Chromosome class, which represents a solution in the genetic algorithm.
"""

from gene import Gene

class Chromosome:
    def __init__(self, values: list[Gene], range_values: list[int] = None):
        self.values = values
        self.length = len(values)
        self.range_values = [] # The values each gene can take
        self.fitness = 0