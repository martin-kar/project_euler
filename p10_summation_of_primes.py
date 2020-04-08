"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math

UPPER_LIMIT = 2 * 10 ** 6


def is_prime(candidate_nbr, lower_primes):
    for prime in lower_primes:
        if prime > math.sqrt(candidate_nbr):
            break
        if candidate_nbr % prime == 0:
            return False
    return True


sum_of_primes = 2
saved_lower_primes = [2]
for nbr in range(3, UPPER_LIMIT, 2):
    if is_prime(nbr, saved_lower_primes):
        sum_of_primes += nbr
        saved_lower_primes.append(nbr)
print(sum_of_primes)
