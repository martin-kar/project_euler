"""
Lattice paths
Problem 15

First we realize that there are
40!/(20!*20!) ways to order two different directions of 20 each, in
a sequence with total length 40.
"""

import math

GRID_SIZE = 20

nbr_of_combinations = math.factorial(2 * GRID_SIZE) / math.factorial(GRID_SIZE) ** 2
print(nbr_of_combinations)
