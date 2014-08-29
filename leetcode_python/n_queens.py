
n = 4
solutions = []
x_s = range(n) # initialize x positions


def find_y_for_next_queen(previous, level):
    current = []
    for i in range(n):
        if i not in previous and not any(abs(x_s[p] - x_s[level]) == abs(previous[p] - i) for p in range(level)):
            current.append(tuple(previous + [i]))
    return current


previous_lst = [[]]
for level in range(n):
    current_set = []
    for previous in previous_lst:
        current_set.extend(find_y_for_next_queen(previous, level))
