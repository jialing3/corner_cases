from itertools import combinations, permutations

# outer represents the nodes on the outer ring
# inner represents the nodes on the inner ring
# on the inner ring, middle represents the nodes in the middle of a line
# on the inner ring, end_node represents the nodes on the end of a line

lst = range(1, 11)
numbers = []
for inner in combinations(lst, 5):
    total = 55 + sum(inner)
    if total % 5 == 0:
        line_sum = total / 5
        outer = list(set(lst) - set(inner))
        for middle in permutations(inner):
            end_node = [line_sum - mid - out for mid, out in zip(middle, outer)]
            if sorted(end_node) == sorted(middle) and all(e != m for e, m in zip(end_node, middle)): # no elements used more than twice and no elements used twice on a line
                table = zip(outer, middle, end_node)
                table.sort(reverse=True)
                table = table[-1:] + table[:-1]
                digits = ''.join(str(num) for line in table for num in line)
                if len(digits) == 16:
                    numbers.append(int(digits))

print max(numbers)
