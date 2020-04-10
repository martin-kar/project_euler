"""
Maximum path sum I
Problem 18
Find the maximum total from top to bottom of the triangle below.
NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)
"""

data = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


# Let's be smart! We don't exhaust all possible paths. Instead we
# formulate a "cumulative triangle" from below, where each value 
# indicates the max remaining value given that we take the optimal
# path from there. Similar techniques are used in reinforcement 
# learning and motion planning. Since this strategy scales well
# with the triangle size, we will do the same later in problem 67 :)


def get_cumulative_row(cumulative_triangle, row_index, row):
    previous_cumulative_row = cumulative_triangle[row_index - 1]
    new_cumulative_row = []
    for nbr_index, nbr in enumerate(row):
        new_cumulative_row.append(
            int(nbr) + max(previous_cumulative_row[nbr_index], previous_cumulative_row[nbr_index + 1]))
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


def get_maximum_sum():
    all_rows = data.splitlines()
    cumulative_triangle = get_cumulative_triangle(all_rows)
    return cumulative_triangle[-1][0]


print(get_maximum_sum())
