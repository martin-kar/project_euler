"""
Highly divisible triangular number
Problem 12
What is the value of the first triangle number to have over five hundred divisors?
"""

import numpy as np


REQUIRED_NUMBER_OF_DIVISORS = 500


def get_non_zero_multiplicities(nbr, primes):
    multiplicities = []
    for prime in primes:
        multiplicity = get_multiplicity(prime, nbr)
        if multiplicity > 0:
            multiplicities.append(multiplicity)
    return multiplicities


def get_multiplicity(factor, nbr_to_factorize):
    multiplicity = 0
    while nbr_to_factorize % factor == 0 and nbr_to_factorize > 0:
        multiplicity += 1
        nbr_to_factorize /= factor
    return multiplicity


def get_nbr_of_divisors(nbr, primes):
    multiplicities = get_non_zero_multiplicities(nbr, primes)
    return np.prod(np.array(multiplicities) + 1)


def get_primes():
    primes = [2, 3]
    nbr = 3
    while len(primes) < REQUIRED_NUMBER_OF_DIVISORS:
        nbr += 2
        if is_prime(nbr, primes):
            primes.append(nbr)
    return primes


def is_prime(nbr, saved_primes):
    for prime in saved_primes:
        if prime ** 2 > nbr:
            return True
        if nbr % prime == 0:
            return False
    return True


def get_divisible_nbr():
    primes = get_primes()
    natural_nbr = 1
    triangle_nbr = 1
    largest = 0
    while True:
        nbr_of_divisors = get_nbr_of_divisors(triangle_nbr, primes)
        if nbr_of_divisors > largest:
            largest = nbr_of_divisors
        if nbr_of_divisors > REQUIRED_NUMBER_OF_DIVISORS:
            return triangle_nbr
        natural_nbr += 1
        triangle_nbr += natural_nbr


print(get_divisible_nbr())
