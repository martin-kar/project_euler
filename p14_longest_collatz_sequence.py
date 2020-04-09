"""
Longest Collatz sequence
Problem 14
Which starting number, under one million, produces the longest
Collatz sequence?
"""

MAX_START_NUMBER = 10 ** 6


def get_record_number():
    record_length = 1
    record_number = 1
    for starting_number in range(2, MAX_START_NUMBER):
        sequence_length = get_sequence_length(starting_number)
        if is_new_record(sequence_length, record_length):
            record_length = sequence_length
            record_number = starting_number
    return record_number


def get_sequence_length(starting_number):
    sequence_length = 1
    n = starting_number
    while n > 1:
        n = get_collatz_update(n)
        sequence_length += 1
    return sequence_length


def is_new_record(sequence_length, record_length):
    return sequence_length > record_length


def get_collatz_update(n):
    if n % 2 == 0:
        n_next = n / 2
    else:
        n_next = 3 * n + 1
    return n_next


print(get_record_number())
