filename = 'p067_triangle.txt'
# greedy

sum_row = [0, 0]
with open(filename) as f:
    for row in f.xreadlines():
        row = row.strip().split(' ')
        sum_row = [0] + [max(sum_row[ind], sum_row[ind + 1]) + int(num) for ind, num in enumerate(row)] + [0]

print max(sum_row)
