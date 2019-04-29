'''
Maximum path sum II
Problem 67
'''

f = open("p067_triangle.txt",'r')
data = f.read()
print(data)

def get_cumulative_row(cumulative_triangle, row_index, row):
	previous_cumulative_row = cumulative_triangle[row_index-1]
	new_cumulative_row = []
	for nbr_index, nbr in enumerate(row):
		new_cumulative_row.append(int(nbr) + max(previous_cumulative_row[nbr_index], previous_cumulative_row[nbr_index+1]))
	return new_cumulative_row
	

def get_cumulative_triangle(all_rows):
	cumulative_triangle = []
	for row_index, row in enumerate(reversed(all_rows)):
		row = row.split()
		if row_index == 0:
			cumulative_triangle.append([int(nbr) for nbr in row])
		else:
			cumulative_triangle.append(get_cumulative_row(cumulative_triangle, row_index, row))
	return cumulative_triangle
		

def get_maximum():
	all_rows = data.splitlines()
	cumulative_triangle = get_cumulative_triangle(all_rows)
	#return get_maximum(cumulative_triangle)
	print(cumulative_triangle[-1])
get_maximum()
#print(get_maximum())
