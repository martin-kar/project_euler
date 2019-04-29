'''
Largest palindrome product
Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest = 0
# Formalize 3-digit number boundaries:
start = 100
stop = 999

# Check if palindrome:
def is_palindrome(nbr):
	return nbr == int(str(nbr)[::-1])

# Iterate over all 3-digit numbers, for each of the two factors:
for a in range(start,stop+1): 
	for b in range(start,stop+1):
		product = a*b # This is the product.
		# It's only interesting if it's a potential new record:
		if product > largest:
			# Check if it is also a palindrome. In that case, we update
			# the record (largest).
			if is_palindrome(product):
				largest = product
				
print(largest)
