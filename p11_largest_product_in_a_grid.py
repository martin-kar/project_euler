"""
Largest product in a grid
Problem 11
Find largest product of four elements in the grid, that are diagonal,
horizontal, or vertical neighbors.
"""

import numpy as np

GRID_STRING = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 "
GRID_SIZE = 20
NEIGHBOR_SEQUENCE_LENGTH = 4
NUMBER_LENGTH = 2
TOKENS_PER_NUMBER_INCLUDING_SPACE = 3


def get_grid():
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for row_nbr in range(GRID_SIZE):
        for column_nbr in range(GRID_SIZE):
            number = get_number(row_nbr, column_nbr)
            grid[row_nbr, column_nbr] = number
    return grid


def get_number(row_nbr, column_nbr):
    tokens_in_above_rows = row_nbr * GRID_SIZE * TOKENS_PER_NUMBER_INCLUDING_SPACE
    grid_start_index = tokens_in_above_rows + column_nbr * TOKENS_PER_NUMBER_INCLUDING_SPACE
    grid_stop_index = tokens_in_above_rows + column_nbr * TOKENS_PER_NUMBER_INCLUDING_SPACE + NUMBER_LENGTH
    number_string = GRID_STRING[grid_start_index: grid_stop_index]
    return int(number_string)


GRID = get_grid()


def get_largest_horizontal_product():
    largest = 0
    for row_nbr, row in enumerate(GRID):
        for column_nbr, column in enumerate(row):
            if column_nbr + NEIGHBOR_SEQUENCE_LENGTH > GRID_SIZE:
                break
            prod = np.prod(row[column_nbr:column_nbr + NEIGHBOR_SEQUENCE_LENGTH])
            largest = max(prod, largest)
    return largest


def get_largest_vertical_product():
    largest = 0
    for row_nbr, row in enumerate(GRID):
        if row_nbr + NEIGHBOR_SEQUENCE_LENGTH > GRID_SIZE:
            break
        for column_nbr, column in enumerate(row):
            prod = np.prod(GRID[row_nbr:row_nbr:NEIGHBOR_SEQUENCE_LENGTH, column_nbr])
            largest = max(prod, largest)
    return largest


def get_largest_diagonal_down_right_product():
    largest = 0
    for row_nbr, row in enumerate(GRID):
        if row_nbr + NEIGHBOR_SEQUENCE_LENGTH > GRID_SIZE:
            break
        for column_nbr, column in enumerate(row):
            if column_nbr + NEIGHBOR_SEQUENCE_LENGTH > GRID_SIZE:
                break
            prod = GRID[row_nbr, column_nbr] * GRID[row_nbr + 1, column_nbr + 1] * GRID[row_nbr + 2, column_nbr + 2] * GRID[
                row_nbr + 3, column_nbr + 3]
            largest = max(prod, largest)
    return largest


def get_largest_diagonal_down_left_product():
    largest = 0
    for row_nbr, row in enumerate(GRID):
        if row_nbr + NEIGHBOR_SEQUENCE_LENGTH > GRID_SIZE:
            print(row_nbr)
            break
        for column_nbr, column in enumerate(row):
            print(column_nbr - NEIGHBOR_SEQUENCE_LENGTH)
            if column_nbr - NEIGHBOR_SEQUENCE_LENGTH < 0:
                continue
            prod = GRID[row_nbr, column_nbr] * GRID[row_nbr + 1, column_nbr - 1] * GRID[row_nbr + 2, column_nbr - 2] * GRID[
                row_nbr + 3, column_nbr - 3]
            largest = max(prod, largest)
    return largest


def get_largest_product():
    largest_horizontal_product = get_largest_horizontal_product()
    largest_vertical_product = get_largest_vertical_product()
    largest_diagonal_down_right_product = get_largest_diagonal_down_right_product()
    largest_diagonal_down_left_product = get_largest_diagonal_down_left_product()
    largest_product = max(largest_horizontal_product, largest_vertical_product, largest_diagonal_down_right_product,
                          largest_diagonal_down_left_product)
    return largest_product


def main():
    largest_product = get_largest_product()
    print(largest_product)


if __name__ == '__main__':
    main()
