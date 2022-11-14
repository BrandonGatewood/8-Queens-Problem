# Brandon Gatewood
# CS 441 AI
# Program 2: 8 Queens Problem

# This program uses the genetic algorithm to solve the 8 queens problem

import numpy as np
import scipy as sc
import random
import matplotlib.pyplot as plt


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
    average_fitness = []

    def __init__(self):
        # Generate a random sequence of states for the population size
        for i in range(self.population_size):
            for j in range(self.num_of_queens):
                self.population[i][j] = random.randrange(1, self.num_of_queens + 1)

    # Fitness function, calculates the maximum number of distinct pairs of queens that aren't attacking
    def fitness(self, parent):
        score = 0
        for i in range(self.num_of_queens):
            col = parent[i]
            for j in range(self.num_of_queens):
                if j == i:
                    continue
                if parent[j] == col:
                    continue
                if j + parent[j] == i + col:
                    continue
                if j - parent[j] == i - col:
                    continue
                score += 1
        return score / 2

    # Selection function, selects two individuals to become parents and breed two children. Parents are randomly
    # selected based on their fitness score.
    def selection(self):
        parents = []
        prob = np.zeros(self.population_size)

        # Calculate the fitness score of each individual in the population
        for i in range(self.population_size):
            prob[i] = self.fitness(self.population[i])

        # Save the average fitness found in the population
        self.average_fitness.append(sum(prob) / len(prob))

        # Calculate the probability of picking each individual
        prob = prob / sum(prob)

        # Randomly select two individuals to breed
        index1 = np.random.choice(self.population_size, p=prob)
        index2 = np.random.choice(self.population_size, p=prob)

        parents.append(self.population[index1])
        parents.append(self.population[index2])
        return parents

    # Crossover function, randomly selects an int from 0 - num_of_queens. This will be used to determine where to split
    # parent 1 and parent 2. For this project, two parents will breed two children.
    def crossover(self, parents):
        children = []
        # Randomly select an index to crossover and breed children
        crossover_index1 = random.randrange(self.num_of_queens)
        x = parents[0][:crossover_index1]
        y = parents[1][crossover_index1:]
        crossover_index2 = random.randrange(self.num_of_queens)
        i = parents[0][:crossover_index2]
        j = parents[1][crossover_index2:]
        children.append(np.concatenate((x, y)))
        children.append(np.concatenate((i, j)))

        return children

    # Randomly mutate one gene of new child
    def mutate_child(self, child):
        index = random.randrange(0, self.num_of_queens)
        new_gene = random.randrange(1, self.num_of_queens)

        child[index] = new_gene

        return child

    # Evolution function, when a solution hasn't been found then a new generation must be born. This function calls the
    # selection and crossover function to create new children that will replace two individuals in the current
    # population with the lowest fitness score. Before entering the population, a single gene from each child may be
    # randomly mutated
    def evolution(self):
        # Select two individuals to become parents
        parents = self.selection()

        # Crossover to breed children
        children = self.crossover(parents)

        # Children mutation
        mutate1 = np.random.choice((1, 0), p=(0.20, 0.80))
        mutate2 = np.random.choice((1, 0), p=(0.20, 0.80))

        if mutate1 == 1:
            children[0] = self.mutate_child(children[0])
        if mutate2 == 1:
            children[1] = self.mutate_child(children[1])

        # Introduce children to the population and remove 2 individuals with the lowest fitness score
        new_generation = children

        for i in self.population:
            new_generation.append(i)

        # Remove two individuals from the population with the lowest fitness score
        new_generation = sorted(new_generation, key=lambda key: self.fitness(key), reverse=True)[:self.population_size]

        return np.array(new_generation)

    # Run the genetic algorithm to find a solution to the 8 queens problem
    def run(self):
        generation = 0
        while not self.check_for_solution(generation):
            print("Generation: " + str(generation))
            self.population = self.evolution()
            generation += 1

    # Check each generation to see if 8 queens problem has been solved, the sequence contains all distinct values. Once
    # a solution has been found the program will display a graph to evaluate the performance.
    def check_for_solution(self, generations):
        print(self.population)
        for i in self.population:
            score = self.fitness(i)
            if score == sc.special.comb(self.num_of_queens, 2):
                print("Solution found: ")
                print(i)
                self.plot(generations)
                return True
        return False

    # Graph that evaluates the genetic algorithms performance.
    def plot(self, generations):
        generation = [x for x in range(generations)]
        plt.plot(generation, self.average_fitness)
        plt.ylabel("Average Fitness Score")
        plt.xlabel("Generation Number")
        plt.title("One Run of the Genetic Algorithm")

        plt.show()


# Run the genetic algorithm to solve the 8 queens problem
run = GA()
run.run()
