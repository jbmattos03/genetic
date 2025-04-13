"""
This module defines the FitnessFunction class, which is used to evaluate the fitness of a chromosome in a genetic algorithm.
"""

class FitnessFunction:
    def __init__(self, max_sum: int,  cost_values: list[int], range_values: list[int], price_values: list[int]):
        """
        Initializes the fitness function with the given parameters.
        :param max_sum: The maximum sum constraint for the fitness function.
        :param range_values: The range of values for each gene in the chromosome (constraints for x1, ..., xn).
        :param price_values: The price values associated with each gene in the chromosome.
        :param cost_values: The cost values associated with each gene in the chromosome.
        """
        self.max_sum = max_sum
        self.cost_values = cost_values
        self.range_values = range_values
        self.price_values = price_values
