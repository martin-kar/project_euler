'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
'''

# NOTE: Just multiplying the numbers 1 to 20 gives a number that 
# is indeed divisible by all of them, but it would be unnecessarily
# large.

max_divisor = 20

# Takes integer nbr, returns all factors (not just primes).
def factorize(nbr):
	factors = []
	i = 2
	while nbr > 1:
		if nbr%i==0:
			factors.extend([i])
			nbr = nbr/i
		else:
			i = i+1
	return factors

# List of factors for each integer up to max_divisor (inclusive).
all_factors = []
for i in range(2,max_divisor+1):
	all_factors.append(factorize(i))

# Stores the multiplicity of each factor. Initialized to zeros.
nbr_of_each_factor = [0]*(max_divisor-1)

# The following loop will for each factor, store the largest 
# multiplicity of that factor among the numbers 1 to 20.
# The value is stored in nbr_of_each_factor. The index corresponds to
# the factor.
# Iterate over each divisor from 2 to max_divisor:
for divisor in range(2,max_divisor+1):
	# Iterate over the numbers from 2 to max_divisor:
	for i in range(2,max_divisor+1):
		if all_factors[divisor-2].count(i) > nbr_of_each_factor[i-2]:
			print(divisor) # Print for sanity check.
			print(nbr_of_each_factor[i-2]) # Print for sanity check.
			all_factors[divisor-2].count(i)
			nbr_of_each_factor[i-2] = all_factors[divisor-2].count(i)
			print(nbr_of_each_factor[i-2]) # Print for sanity check.



product=1 # Stores the smallest divisible number that we're looking for.
# The product that we're looking for, is just the product of each factor, 
# with multiplicity corresponding to the factor's largest multiplicity
# in any of the numbers 1 to 20, which we stored in nbr_of_each_factor.
for factor in range(2,max_divisor+1):
	product = product* (factor**nbr_of_each_factor[factor-2])

print(product)
