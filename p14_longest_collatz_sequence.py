'''
Longest Collatz sequence
Problem 14
Which starting number, under one million, produces the longest 
Collatz sequence?
'''

longest_length = 1 # Stores record so far.
record_number = 1 # Corresponding starting number for record.

# Search until limit:
for i in range(2,10**6):
	chain_length = 1
	n = i
	print(i)
	while n > 1:
		if n%2==0:
			n /= 2
		else:
			n = 3*n + 1
		chain_length += 1
		# Make some updates if we have a new record: 
		if chain_length > longest_length:
			longest_length = chain_length
			record_number = i
		
print(record_number)
	
