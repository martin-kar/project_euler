"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

# Just multiplying the numbers 1 to 20 gives a number that
# is indeed divisible by all of them, but it would no be the smallest.

MAX_DIVISOR = 20


def get_factors_for_number(nbr):
    factors = []
    i = 2
    while nbr > 1:
        if nbr % i == 0:
            factors.extend([i])
            nbr /= i
        else:
            i += 1
    return factors


def get_all_factors():
    all_factors = []
    for i in range(2, MAX_DIVISOR + 1):
        all_factors.append(get_factors_for_number(i))
    return all_factors


def get_multiplicity_of_each_factor():
    multiplicity_of_each_factor = [0] * (MAX_DIVISOR - 1)
    all_factors = get_all_factors()
    for divisor in range(2, MAX_DIVISOR + 1):
        for i in range(2, MAX_DIVISOR + 1):
            if all_factors[divisor - 2].count(i) > multiplicity_of_each_factor[i - 2]:
                multiplicity_of_each_factor[i - 2] = all_factors[divisor - 2].count(i)
    return multiplicity_of_each_factor


def get_smallest_divisible_number(multiplicity_of_each_factor):
    smallest_divisible_number = 1
    for factor in range(2, MAX_DIVISOR + 1):
        smallest_divisible_number = smallest_divisible_number * (factor ** multiplicity_of_each_factor[factor - 2])
    return smallest_divisible_number


def main():
    multiplicity_of_each_factor = get_multiplicity_of_each_factor()
    smallest_divisible_number = get_smallest_divisible_number(multiplicity_of_each_factor)
    print(smallest_divisible_number)


if __name__ == '__main__':
    main()
