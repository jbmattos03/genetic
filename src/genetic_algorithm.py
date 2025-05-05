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

class GeneticAlgorithm:
    def __init__(self, mutation_rate: float = 0.05, crossover_rate: float = 0.8, fitness_function: FitnessFunction = None):
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

        weight_values = self.fitness_function.weight_values
        max_sum = self.fitness_function.max_sum

        for _ in range(size):
            chromosome = Chromosome(values=[], length=chromosome_length)
            success_flag = False

            while success_flag is False:
                for i in range(chromosome_length):
                    gene = Gene(value=random.randint(0, self.fitness_function.qty_values[i]))
                    chromosome.values.append(gene)
                
                if chromosome not in population and sum([chromosome.values[i].value * weight_values[i] for i in range(chromosome_length)]) <= max_sum:
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
            fitness = 0

            for i in range(chromosome.length):
                fitness += chromosome.values[i].value * self.fitness_function.price_values[i]
            
            chromosome.fitness = fitness
                    
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

        while len(selected) < parents:
            random_number = random.randint(0, total_fitness)
            
            for chromosome in current_pop:
                current_sum += chromosome.fitness

                if random_number < current_sum:
                    selected.append(chromosome)
                    current_pop.remove(chromosome) # Remove parents
                    break # Break out of for loop
                
            current_sum = 0

        # Group selected parents into pairs
        selected = [selected[i:i + 2] for i in range(0, len(selected), 2)]
    
        return selected

    def crossover(self, parent1: Chromosome, parent2: Chromosome, chromosome_length: int = 10, attempts: int = 3, verbose: bool = True):
        """
        Performs crossover between two parents to create two offspring.
        :param parent1: The first parent chromosome.
        :param parent2: The second parent chromosome.
        """
        valid_flag = False
        attempts_counter = attempts

        while valid_flag is False and attempts_counter > 0:
            attempts_counter -= 1

            # Randomly select crossover points
            i = random.randint(0, parent1.length - 1)
            j = random.randint(0, parent2.length - 1)

            if i != j:
                max_index = max(i, j)
                min_index = min(i, j)

                offspring1 = Chromosome(values=parent1.values[:], length=chromosome_length)
                offspring1.values[min_index:max_index] = parent2.values[min_index:max_index][:]

                offspring2 = Chromosome(values=parent2.values[:], length=chromosome_length)
                offspring2.values[min_index:max_index] = parent1.values[min_index:max_index][:]
            else:
                offspring1 = Chromosome(values=parent2.values[:i]+parent1.values[i:], length=chromosome_length)
                offspring2 = Chromosome(values=parent1.values[:i]+parent2.values[i:], length=chromosome_length)


            # Check if the offspring are valid (i.e., their weight does not exceed the max sum)
            # and if they are not already in the population
            if offspring1 not in self.population.chromosomes and offspring2 not in self.population.chromosomes and \
            sum([offspring1.values[k].value * self.fitness_function.weight_values[k] for k in range(chromosome_length)]) <= self.fitness_function.max_sum and \
            sum([offspring2.values[k].value * self.fitness_function.weight_values[k] for k in range(chromosome_length)]) <= self.fitness_function.max_sum:
                valid_flag = True
        
        if valid_flag is True:
            # Replace the parents with the offspring
            parent1.values = offspring1.values
            parent2.values = offspring2.values
        elif valid_flag is False and verbose == True:
            print(f"Crossover failed for parents {[g.value for g in parent1.values]} and {[g.value for g in parent2.values]} after {attempts} attempts.")
            

    def mutate(self, chromosome: Chromosome, verbose: bool = True):
        """
        Mutates a chromosome with a certain probability.
        :param chromosome: The chromosome to mutate.
        """
        for i, g in enumerate(chromosome.values):
            if random.random() <= self.mutation_rate:
                original_value = g.value
                new_value = random.randint(0, self.fitness_function.qty_values[i])

                if new_value != g.value:
                    g.value = new_value

                    # Check if the mutation is valid (i.e., the weight does not exceed the max sum)
                    if any(chromosome.values == pop_chromosome.values for pop_chromosome in self.population.chromosomes) or \
                       sum([chromosome.values[k].value * self.fitness_function.weight_values[k] for k in range(chromosome.length)]) > self.fitness_function.max_sum:
                        g.value = original_value

                        if verbose is True:
                            print(f"Mutation reverted for gene {i} in chromosome {[gene.value for gene in chromosome.values]}.")


    def get_best_solution(self) -> Chromosome:
        """
        Returns the best solution found so far.
        :return: The best chromosome.
        """
        return self.best

    def run(self, generations: int, parents_qty: int, verbose: bool = True):
        """
        Runs the genetic algorithm for a specified number of generations.
        :param generations: The number of generations to run the algorithm.
        :param parents: The number of parents to select for crossover.
        :param verbose: Whether to print the progress of the algorithm or not.
        """
        for _ in range(generations):
            # Increase generation count
            self.generation += 1

            # Get fitness values for each chromosome
            self.evaluate_population()

            # Get parents and do crossover
            parents = self.roulette(parents=parents_qty)
            for parent_tuple in parents:
                if random.random() <= self.crossover_rate:
                    self.crossover(parent_tuple[0], parent_tuple[1], verbose=verbose)
            
            # Do mutation
            for chromosome in self.population.chromosomes:
                self.mutate(chromosome, verbose=verbose)

            if verbose is True:
                print(f"Generation: {self.generation}")
                print(f"Best fitness: {self.best.fitness}")
                print(f"Best chromosome: {[g.value for g in self.best.values]}")

