"""
This module is the main implementation of the Genetic Algorithm.
It includes methods for initializing the population, evaluating fitness, selecting parents, etc.
It uses a simple mutation and crossover strategy to evolve the population.
"""

from gene import Gene
from chromosome import Chromosome
from population import Population
from fitness_function import FitnessFunction

import random

seed = 42
random.seed(seed)  # Set the seed for reproducibility

class GeneticAlgorithm:
    def __init__(self, mutation_rate: float = 0.01, crossover_rate: float = 0.7, fitness_function: FitnessFunction = None):
        self.population = None
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.best = None
        self.generation = 0
        self.fitness_function = fitness_function

    def initialize_population(self, size: int, chromosome_length: int):
        """
        Initializes the population with random chromosomes.
        :param size: The number of chromosomes in the population.
        :param chromosome_length: The length of each chromosome.
        """
        population = []

        range_values = self.fitness_function.range_values
        max_sum = self.fitness_function.max_sum

        for _ in range(size):
            chromosome = Chromosome(values=[], length=chromosome_length)
            success_flag = False

            while success_flag is False:
                for i in range(chromosome_length):
                    gene = Gene(random.randint(0, range_values[i]))
                    chromosome.values.append(gene)
                
                if chromosome not in population and sum([chromosome.values[i].value * range_values[i] for i in range(chromosome_length)]) <= max_sum:
                    success_flag = True
                else:
                    chromosome.values = []

            population.append(chromosome)

        self.population = Population(population)

    def evaluate_population(self):
        """
        Evaluates the fitness of each chromosome in the population.
        :param fitness_function: The function used to evaluate the fitness of a chromosome.
        """
        for chromosome in self.population.chromosomes:
            for i in range(chromosome.length):
                chromosome.fitness += chromosome.values[i].value * self.fitness_function.price_values[i]
                    
            # Ensure fitness is non-negative (unlikely, but just in case)
            if chromosome.fitness < 0:
                chromosome.fitness = 0

        # Update the best solution found so far
        if self.best is None or self.best.fitness < max([chromosome.fitness for chromosome in self.population.chromosomes]):
            self.best = max(self.population.chromosomes, key=lambda x: x.fitness)

    def roulette(self, parents: int) -> list[Chromosome]:
        """
        Selects parents for crossover using roulette selection.
        :return: A list of selected parents.
        """
        selected = []
        current_pop = [chromosome for chromosome in self.population.chromosomes]
        
        total_fitness = sum([chromosome.fitness for chromosome in self.population.chromosomes])
        current_sum = 0

        while current_pop != [] and len(selected) < parents:
            selected_flag = False
            random_number = random.randint(0, total_fitness)
            
            for chromosome in current_pop:
                current_sum += chromosome.fitness

                if random_number < current_sum:
                    selected_flag = True
                    selected.append(chromosome)
                    break
            
            if selected_flag is True:
                current_pop.remove(chromosome)
            current_sum = 0


        # Sort selected parents by fitness
        selected.sort(key=lambda x: x.fitness, reverse=True)

        # Group selected parents into pairs
        selected = [selected[i:i + 2] for i in range(0, len(selected), 2)]
    
        return selected

    def crossover(self, parent1: Chromosome, parent2: Chromosome, chromosome_length: int = 3):
        """
        Performs crossover between two parents to create two offspring.
        :param parent1: The first parent chromosome.
        :param parent2: The second parent chromosome.
        :return: A tuple containing the two offspring chromosomes.
        """
        index = random.randint(1, parent1.length - 1)
        print("Index:", index)

        offspring1 = Chromosome(parent2.values[:index] + parent1.values[index:], chromosome_length)
        offspring2 = Chromosome(parent1.values[:index] + parent2.values[index:], chromosome_length)
        
        parent1.values = offspring1.values
        parent2.values = offspring2.values

    def mutate(self, chromosome: Chromosome):
        """
        Mutates a chromosome with a certain probability.
        :param chromosome: The chromosome to mutate.
        """
        for g in chromosome.values:
            if round(random.random(), 2) <= self.mutation_rate:
                new_value = random.randint(0, self.fitness_function.range_values[chromosome.values.index(g)])

                if new_value != g.value:
                    g.value = new_value

    def get_best_solution(self) -> Chromosome:
        """
        Returns the best solution found so far.
        :return: The best chromosome.
        """
        return self.best

    def run(self, generations: int):
        """
        Runs the genetic algorithm for a specified number of generations.
        :param generations: The number of generations to run the algorithm.
        :param fitness_function: The function used to evaluate the fitness of a chromosome.
        """
        pass

