'''
Factorial digit sum
Problem 20
Find the sum of the digits in the number 100!
'''

import math

# Get 100! as a string:
nbr_str = str(math.factorial(100))

sum = 0
# Iterate accross the string. Add each digit to sum as an integer:
for ch in nbr_str:
	sum += int(ch)
print(sum)
