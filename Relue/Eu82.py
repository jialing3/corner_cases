#!/usr/local/bin/python3

'''
every cell's path can come from left, up or down
'''

data = []

with open('p082_matrix.txt') as f:
    for line in f.readlines():
        line = list(map(int, line.strip().split(',')))
        data.append(line)

curr_column_min = list(map(lambda x: x[0], data))

for col in range(1, len(data[0])):
    # path from left
    for row in range(len(data)):
        curr_column_min[row] += data[row][col]
    # path from up or down
    change_happened = True
    while change_happened:
        change_happened = False
        for row in range(len(data)):
            if row == 0:
                list_to_check = [curr_column_min[row + 1]]
            elif row == len(data) - 1:
                list_to_check = [curr_column_min[row - 1]]
            else:
                list_to_check = [curr_column_min[row - 1], curr_column_min[row + 1]]
            if min(list_to_check) + data[row][col] < curr_column_min[row]:
                curr_column_min[row] = min(list_to_check) + data[row][col]
                change_happened = True

print(min(curr_column_min))
