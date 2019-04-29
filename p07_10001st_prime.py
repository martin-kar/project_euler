'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
see that the 6th prime is 13.
What is the 10 001st prime number?
'''

stored_primes = [2] # Save primes as we find them.
nbr = 2 # Start with first prime.

# Check if nbr is prime. Use stored_primes found previously:
def is_prime(nbr, stored_primes):
	for prime in stored_primes:
		if nbr%prime==0:
			return False
	return True

# Determine primes until we have the 10 001 first ones in order.
while len(stored_primes) <= 10000:
	nbr = nbr+1
	if is_prime(nbr, stored_primes): # Check if nbr is a prime.
		# Save nbr as prime since it is a prime:
		stored_primes.extend([nbr])

# Print last and hence largest prime that we found:
print(stored_primes[-1])
