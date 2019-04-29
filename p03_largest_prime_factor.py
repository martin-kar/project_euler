'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import numpy as np

# Store previously found primes in known_primes:
known_primes = np.array([2])

number2factorize = 600851475143
iteration_limit=number2factorize

# Store prime factors in factors:
factors = np.array([])

# Returns True if and only if nbr is a prime. 
#Uses known primes found previously:
def isprime(nbr, known_primes):
	for prime in known_primes:
		if nbr%prime == 0:
			return False
	return True
	
nbr = 1
while number2factorize > 1:
	# Update number:
	nbr = nbr+1
	
	# Check if nbr is a prime:
	if isprime(nbr,known_primes):
		print(nbr) # Print nbr for sanity check.
		known_primes = np.append(known_primes,nbr) # Save prime
		if number2factorize%nbr == 0: # If nbr is a prime factor:
			factors = np.append(factors,nbr) # Save the prime factor.
			# This prevents us from checking unnecessarily large 
			# values of nbr: 
			number2factorize=number2factorize/nbr 
			
print(factors)
