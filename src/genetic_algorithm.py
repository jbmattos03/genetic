"""
This module is the main implementation of the Genetic Algorithm.
It includes methods for initializing the population, evaluating fitness, selecting parents, etc.
It uses a simple mutation and crossover strategy to evolve the population.
"""

from gene import Gene
from chromosome import Chromosome
from population import Population

import random

seed = 42
random.seed(seed)  # Set the seed for reproducibility

class GeneticAlgorithm:
    def __init__(self):
        self.population = None
        self.mutation_rate = 0.01
        self.crossover_rate = 0.7
        self.best = None
        self.generation = 0

    def initialize_population(self, size: int, chromosome_length: int, fitness_function=None):
        """
        Initializes the population with random chromosomes.
        :param size: The number of chromosomes in the population.
        :param chromosome_length: The length of each chromosome.
        """
        population = []
        max_sum = 20 # Hard coded por enquanto

        for _ in range(size):
            chromosome = Chromosome(range_values=[3, 2, 5])
            success_flag = False

            while success_flag is False:
                for i in range(chromosome_length):
                    gene = Gene(random.randint(0, chromosome.range_values[i]))
                    chromosome.values.append(gene)

                if chromosome not in population and sum([gene.value for gene in chromosome.values]) <= max_sum:
                    success_flag = True

            population.append(chromosome)

        self.population = Population(population)

    def evaluate_population(self, fitness_function):
        """
        Evaluates the fitness of each chromosome in the population.
        :param fitness_function: The function used to evaluate the fitness of a chromosome.
        """
        pass

    def select_parents(self):
        """
        Selects parents for crossover using tournament selection.
        :return: A list of selected parents.
        """
        pass

    def crossover(self, parent1: Chromosome, parent2: Chromosome) -> tuple[Chromosome, Chromosome]:
        """
        Performs crossover between two parents to create two offspring.
        :param parent1: The first parent chromosome.
        :param parent2: The second parent chromosome.
        :return: A tuple containing the two offspring chromosomes.
        """
        index = random.randint(1, parent1.length - 1)

        offspring1 = Chromosome(parent1.values[:index] + parent2.values[index:])
        offspring2 = Chromosome(parent2.values[:index] + parent1.values[index:])

        return tuple(offspring1, offspring2)

    def mutate(self, chromosome: Chromosome):
        """
        Mutates a chromosome with a certain probability.
        :param chromosome: The chromosome to mutate.
        """
        for c in chromosome.values:
            success_flag = False

            while success_flag is False:
                if round(random.random(), 2) <= self.mutation_rate:
                    new_value = random.randint(0, chromosome.range_values[chromosome.values.index(c)])

                    if new_value != c.value:
                        c.value = new_value
                        success_flag = True
                        


    def get_best_solution(self) -> Chromosome:
        """
        Returns the best solution found so far.
        :return: The best chromosome.
        """
        return self.best

    def run(self, generations: int, fitness_function):
        """
        Runs the genetic algorithm for a specified number of generations.
        :param generations: The number of generations to run the algorithm.
        :param fitness_function: The function used to evaluate the fitness of a chromosome.
        """
        pass

