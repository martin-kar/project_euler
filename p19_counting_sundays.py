"""
Counting sundays
Problem 19
How many sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

DAYS_PER_WEEK = 7
SUNDAY = 7
DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS_PER_YEAR = 12


def get_days_this_month(month, year):
    if is_leap_day(month, year):
        return 29
    else:
        return DAYS_PER_MONTH[month - 1]


def is_leap_day(month, year):
    return (month == 2) and (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


def is_synday_the_first_this_month(day_of_week, day_of_month):
    return (day_of_week == SUNDAY) & (day_of_month == 1)


def get_next_day_of_week(day_of_week):
    if day_of_week == SUNDAY:
        next_day_of_week = 1
    else:
        next_day_of_week = day_of_week + 1
    return next_day_of_week


def should_increase_month(day_of_month, days_this_month):
    return day_of_month + 1 > days_this_month


def should_increase_year(month):
    return month + 1 > MONTHS_PER_YEAR


def get_next_date(year, month, day_of_month):
    days_this_month = get_days_this_month(month, year)
    if should_increase_month(day_of_month, days_this_month):
        next_day_of_month = 1
        if should_increase_year(month):
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
    else:
        next_day_of_month = day_of_month + 1
        next_month = month
        next_year = year
    return next_year, next_month, next_day_of_month


def get_number_of_sundays_on_first_of_month():
    day_of_week = 2
    day_of_month = 1
    year = 1901
    month = 1
    nbr_sundays_on_first_of_month = 0
    while year <= 2000:
        if is_synday_the_first_this_month(day_of_week, day_of_month):
            nbr_sundays_on_first_of_month += 1

        day_of_week = get_next_day_of_week(day_of_week)
        year, month, day_of_month = get_next_date(year, month, day_of_month)
    return nbr_sundays_on_first_of_month


print(get_number_of_sundays_on_first_of_month())
