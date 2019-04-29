'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

lower_primes = [] # Stores primes found so far.

# Checks whether nbr is prime, using previously found primes:
def isprime(nbr, lower_primes):
	for prime in lower_primes:
		if nbr%prime == 0:
			return False
	return True

upper_limit = 2*10**6
sum = 0

for nbr in range(2,upper_limit):
	print(nbr)
	# If nbr is a prime, we add it to the sum and 
	# save it in lower_primes:
	if isprime(nbr, lower_primes):
		sum += nbr
		lower_primes.extend([nbr])

print(sum)
