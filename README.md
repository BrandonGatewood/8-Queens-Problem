# 8 Queens Problem
This program uses the genetic algortihm to solve the 8 queens problem.

# Core Elements of The Genetic Agorithm:
Fitness function: the maximum number of distinct pairs of queens that can be mutually attacking at any one time.

Initial Population: The initialization contains a randomly distributed population.

Selection of parents: Two parents are selected to determine a child; this selection is in proportion to the “fitness” of each parent. 

CrossOver: Once parents having high fitness are selected, crossover essentially marks the recombining of genetic materials / chromosomes to produce a healthy offspring. Pick a random spot for crossover, and breed two new children (with fitness computed). 

Mutation: Mutation may or may not occur. In case mutation occurs, it forces a random value of child to change. Randomly decide whether to mutate based on a MutationPct, and if so, mutate one gene.
