"""
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
"""

ZERO_TO_TWENTY_AS_WORDS = ["", "one", "two", "three", "four", "five", "six",
                           "seven", "eight", "nine", "ten", "eleven", "twelve",
                           "thirteen", "fourteen", "fifteen", "sixteen",
                           "seventeen", "eighteen", "nineteen", "twenty"]

TENTH_PREFIXES = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
                  "seventy", "eighty", "ninety"]


def get_number_of_letters_below_hundred(nbr):
    if nbr <= 20:
        return len(ZERO_TO_TWENTY_AS_WORDS[nbr])
    else:
        return len(TENTH_PREFIXES[nbr // 10]) + len(
            ZERO_TO_TWENTY_AS_WORDS[nbr % 10])


def get_number_of_letters_below_thousand(nbr):
    if nbr < 100:
        return get_number_of_letters_below_hundred(nbr)
    elif nbr % 100 == 0:
        return len(ZERO_TO_TWENTY_AS_WORDS[nbr // 100]) + len("hundred")
    else:
        return len(ZERO_TO_TWENTY_AS_WORDS[nbr // 100]) + len("hundred") + len(
            "and") + get_number_of_letters_below_hundred(nbr % 100)


def get_number_of_letters(nbr):
    if nbr == 1000:
        return len("one") + len("thousand")
    else:
        return get_number_of_letters_below_thousand(nbr)


def get_total_number_of_letters():
    nbr_of_letters = 0
    for i in range(1, 1001):
        nbr_of_letters += get_number_of_letters(i)
    return nbr_of_letters


print(get_total_number_of_letters())
