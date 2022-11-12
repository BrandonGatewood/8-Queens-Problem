# Brandon Gatewood
# CS 441 AI
# Program 2: 8 Queens Problem

# This program uses the genetic algorithm to solve the 8 queens problem

import numpy as np
import random


# Class contains the genetic algorithm to solve the 8 queens problem.
class GA:
    # initialize the number of queens, population size and a nxn matrix to represent the queens, experiment with
    # different population sizes
    num_of_queens = 8
    population_size = 10
    # population_size = 100
    # population_size = 500
    # population_size = 1000
    population = np.zeros(shape=(population_size, num_of_queens))

    def __init__(self):
        # Generate a random sequence for the population size
        for i in range(self.population_size):
            for j in range(self.num_of_queens):
                self.population[i][j] = random.randrange(1, self.num_of_queens + 1)

    # Fitness function, maximum number of distinct pairs of queens that aren't attacking
    def fitness(self):
        p1_len = 0
        p1 = 0
        p2_len = 0
        p2 = 0

        for i in range(self.population_size):
            parent_len = len(np.unique(self.population[i]))
            if parent_len > p1_len:
                p2_len = p1_len
                p2 = p1
                p1 = i
                p1_len = parent_len
            elif parent_len > p2_len:
                p2_len = parent_len
                p2 = i

        return p1, p2

    def run(self):
        # run the algorithm for 10 generations
        for i in range(10):
            # Select two random parents to breed based on the fitness function
            p1, p2 = self.fitness()

            # Randomly select a spot to crossover and breed two new children. Once a child has been born, randomly
            # decide to mutate; 1, 0. 1, mutate a random mutate a gene. 0, do not mutate child.
            crossover = random.randrange(0, self.num_of_queens)


    def print_table(self):
        print(self.population)


run = GA()
run.print_table()
run.run()
