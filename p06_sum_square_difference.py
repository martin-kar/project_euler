'''
Sum square difference
Problem 6
Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
'''

first = 1
last = 100

def get_sum_of_squares(first,last):
	sum_of_squares = 0
	for i in range(first,last+1):
		sum_of_squares = sum_of_squares + i**2
	return sum_of_squares
	
def get_square_of_sum(first, last):
	all_numbers = range(first, last+1)
	return sum(all_numbers)**2

sum_of_squares = get_sum_of_squares(first, last)
square_of_sum = get_square_of_sum(first, last)

# Difference we're looking for:
diff = square_of_sum - sum_of_squares

print(diff)
