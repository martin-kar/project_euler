'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, 
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in 
compliance with British usage.
'''

# Store numbers as words. Use combinations to write larger numbers,
# like "twenty three" is "twenty" and "three".
zero_to_twenty = ["", "one", "two", "three", "four", "five", "six",
"seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
"fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
"twenty"]

# Tenth prefixes used as building blocks.
tenth_prefixes = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
"seventy", "eighty", "ninety"]

# Counts letters of numbers below one hundred:
def below_hundred(nbr):
	if nbr <= 20:
		return len(zero_to_twenty[nbr])
	else:
		return len(tenth_prefixes[nbr//10]) + len(zero_to_twenty[nbr%10])

# Counts letters of numbers below one thousand:
def below_thousand(nbr):
	if nbr < 100:
		return below_hundred(nbr)
	elif nbr%100==0:
		return len(zero_to_twenty[nbr//100]) + len("hundred")
	else:
		return len(zero_to_twenty[nbr//100]) + len("hundred") + len("and") + below_hundred(nbr%100)

# Counts letters of numbers up to one thousand (inclusive):
def get_length(nbr):
	if nbr == 1000:
		return len("one") + len("thousand")
	else:
		return below_thousand(nbr)

# Add all letters from all numbers to nbr_letters:
nbr_letters = 0
for i in range(1,1001):
	print(i, get_length(i))
	nbr_letters += get_length(i)

print(nbr_letters)
