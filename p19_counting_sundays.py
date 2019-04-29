'''
Counting Sundays
Problem 19
How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
'''

days_per_week = 7
sunday = 7 # Days of week are represented as integers.
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays_on_first = 0 # We add to this number everytime we find such day.
months_per_year = 12

# Returns number of days in month, given the year.
def get_days_this_month(month, year):
	if (month==2) & (year%4==0) & ( (year%100!=0) | (year%400==0) ): 
		return 29 # Leap day.
	else:
		return days_per_month[month-1] # No leap day.

# Initialize loop
day_of_week = 2
day_of_month = 1
year = 1901
month = 1

# Add number of sundays on the 1st of a month
# up until year 2000 (inclusive):
while year <= 2000:
	
	# Count Sunday the 1st:
	if (day_of_week == sunday) & (day_of_month == 1):
		sundays_on_first += 1
		print(day_of_week, day_of_month, month, year)
	
	# Update day of week:
	if day_of_week == sunday:
		day_of_week = 1
	else:
		day_of_week += 1

	# Update day, month and year:
	days_this_month = get_days_this_month(month, year)
	day_of_month += 1
	if day_of_month > days_this_month:
		month += 1
		day_of_month = 1
		if month > months_per_year:
			year += 1
			month = 1

print(sundays_on_first)
