
    # @return a list of lists of length 3, [[val1,val2,val3]]
def threeSum(num):

    num_dict = {}

    for i, a in enumerate(num):
        if a not in num_dict:
            num_dict[a] = set()
        num_dict[a].add(i)

    solutions = set()

    for i, a in enumerate(num):
        for j, b in enumerate(num):
            if i < j:
                c = 0 - a - b
                if c in num_dict:
                    k_list = num_dict[c]
                    if any([k != i and k != j for k in k_list]):
                        solutions.add(tuple(sorted((a, b, c))))

    return [list(row) for row in solutions]


num = [0, 0, 0]

print threeSum(num)
