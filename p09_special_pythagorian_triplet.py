'''
Special Pythagorean triplet
Problem 9

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# Takes integers a,b,c. Returns boolean of whether a,b,c is Pythagorean 
# triplet:
def is_pyth_triplet(a,b,c):
	return (a**2 + b**2 == c**2) & (a<b) & (b<c)

abc = 0


found = False # We know there is exactly 1 triplet. 
# found indicates whether the triplet is found, so we can stop 
# searching.

# Run the search:
for a in range(1,1000):
	print(a)
	if found:
		break
	for b in range(a+1,1000):
		for c in range(b+1,1000):
			if is_pyth_triplet(a,b,c) & ( (a+b+c)==1000):
				print (a,b,c)
				abc = a*b*c
				found = True
print(abc)
