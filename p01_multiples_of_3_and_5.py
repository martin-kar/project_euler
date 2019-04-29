'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum = 0
for nbr in range(1,1000):
	# Add to sum if nbr is multiple of 3 or 5.
	if nbr%3==0:
		sum = sum+nbr
	elif nbr%5==0:
		sum = sum+nbr

print(sum)

	
