"""
This module defines the Population class, which represents a collection of chromosomes in the genetic algorithm.
"""

from chromosome import Chromosome

class Population:
    def __init__(self, chromosomes: list[Chromosome]):
        self.chromosomes = chromosomes
        self.size = len(chromosomes)