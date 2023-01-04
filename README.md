# This program uses a genetic algorithm that solves the 8-queens problem

The program will start by creating PopulationSize random members of the population (including a computation of the fitness function for each one). The program will loop iteratively NumIterations times, performing the following functions:
• Randomly select pairs of parents to breed. 
• Pick a random spot for crossover, and breed two new children (with fitness computed). 
• Randomly decide whether to mutate based on MutationPct, and if so, mutate one gene. 
• Generate a sufficient number of children to keep the population size constant.


Fitness function: the maximum number of distinct pairs of queens that can be mutually attacking at any one time.

Initial Population: The initialization contains a randomly distributed population.

Selection of parents: Two parents are selected to determine a child; this selection is in proportion to the “fitness” of each parent. 

CrossOver: Once parents having high fitness are selected, crossover essentially marks the recombining of genetic materials / chromosomes to produce a healthy offspring. Pick a random spot for crossover, and breed two new children (with fitness computed). 

Mutation: Mutation may or may not occur. In case mutation occurs, it forces a random value of child to change. Randomly decide whether to mutate based on a MutationPct, and if so, mutate one gene.
