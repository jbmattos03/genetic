"""
This is the main module for the genetic algorithm.
It creates an instance of the GeneticAlgorithm class and runs the algorithm.
"""

from genetic_algorithm import GeneticAlgorithm
from fitness_function import FitnessFunction

import random

def main():
    fitness_function = FitnessFunction(max_sum=15, 
                                       weight_values=[2, 3, 4, 5, 7, 1, 6, 4.5, 3.5, 2.5], 
                                       price_values=[40, 50, 65, 80, 110, 15, 90, 70, 60, 55])
    
    gen_alg = GeneticAlgorithm(fitness_function=fitness_function)
    gen_alg.initialize_population(size=50, chromosome_length=10)

    gen_alg.run(generations=200, 
                parents_qty=40,
                verbose=False
                )

    solution = gen_alg.get_best_solution()

    print("==========================================================")
    print(f"Best solution: {[g.value for g in solution.values]}")
    print(f"Weight: {sum([solution.values[i].value*fitness_function.weight_values[i] for i in range(solution.length)])}")
    print(f"Fitness: {solution.fitness}")
    print("==========================================================")

if __name__ == "__main__":
    main()