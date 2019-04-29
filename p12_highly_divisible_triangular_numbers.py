'''
Highly divisible triangular number
Problem 12
What is the value of the first triangle number to have over five hundred divisors?
'''

import numpy as np

# Returns multiplicities, which is the multiplicity of each prime in 
# primes given the integer nbr:
def get_multiplicities(nbr, primes):
	multiplicities = np.array([])
	for prime in primes:
		multiplicity = 0
		if prime > nbr:
			break
		while nbr%prime == 0:
			multiplicity += 1
			nbr /= prime
		if multiplicity > 0:
			multiplicities = np.append(multiplicities,multiplicity)
	return multiplicities

# Returns the total number of divisors of integer nbr:
def nbr_divisors(nbr, primes):
	multiplicities = get_multiplicities(nbr, primes)
	return np.prod(multiplicities+1)
	
# Prepare a list of primes (named primes) up to max_nbr.
def prepare_primes(max_nbr):
	primes = [2]	
	nbr = 2
	while len(primes) < max_nbr:
		nbr_is_prime = True
		for prime in primes:
			if nbr%prime == 0:
				nbr_is_prime = False
		if nbr_is_prime:
			primes.extend([nbr])
		nbr += 1
	return primes

# Given integer max_nbr_of_divisors, returns number with that 
# amount of divisors.
def get_divisible_nbr(max_nbr_of_divisors):
	primes = prepare_primes(max_nbr_of_divisors)
	natural_nbr = 1
	triangle_nbr = 1
	largest = 0
	while True:
		nbr_of_divisors = nbr_divisors(triangle_nbr, primes)
		if nbr_of_divisors > largest:
			largest = nbr_of_divisors
			print(largest)
		if nbr_of_divisors > max_nbr_of_divisors:
			return triangle_nbr
		natural_nbr += 1
		triangle_nbr += natural_nbr

print(get_divisible_nbr(500))
