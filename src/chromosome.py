"""
This module defines the Chromosome class, which represents a solution in the genetic algorithm.
"""

from gene import Gene

class Chromosome:
    def __init__(self, values: list[Gene], length: int):
        self.values = values
        self.length = length
        self.fitness = 0