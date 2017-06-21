#!/usr/local/bin/python3
from itertools import accumulate

data = []

with open('p081_matrix.txt') as f:
    for line in f.readlines():
        line = list(map(int, line.strip().split(',')))
        data.append(line)

current_row_with_min = list(accumulate(data[0]))

for row in data[1:]:
    for ind, element in enumerate(row):
        if ind == 0:
            current_row_with_min[ind] += element
        else:
            current_row_with_min[ind] = min(current_row_with_min[ind - 1],
                                            current_row_with_min[ind]) + element

print(current_row_with_min[-1])
