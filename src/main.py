"""
This is the main module for the genetic algorithm.
It creates an instance of the GeneticAlgorithm class and runs the algorithm.
"""

from genetic_algorithm import GeneticAlgorithm

def main():
    gen_alg = GeneticAlgorithm()
    gen_alg.initialize_population(size=10, chromosome_length=3)

    #gen_alg.run()

if __name__ == "__main__":
    main()