'''
Power digit sum
Problem 16
What is the sum of the digits of the number 2 to the power of 1000?
'''

number = str(2**1000) # The number converted to a string.
sum = 0
for ch in number: # Iterate over string:
	sum += int(ch) # Add each digit to sum.

print(sum)

