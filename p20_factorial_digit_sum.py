"""
Factorial digit sum
Problem 20
Find the sum of the digits in the number 100!
"""

import math

nbr_str = str(math.factorial(100))
sum_of_digits = sum([int(c) for c in nbr_str])
print(sum_of_digits)
