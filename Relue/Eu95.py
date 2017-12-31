
def get_divisor_sums(upper_bound):
    divisor_sums = [1 for i in range(upper_bound + 1)]
    divisor_sums[0] = 0
    divisor_sums[1] = 0
    for i in range(2, upper_bound + 1):
        for j in range(2 * i, upper_bound + 1, i):
            divisor_sums[j] += i
    return divisor_sums

assert(get_divisor_sums(28) == [0, 0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10,
                                9, 15, 1, 21, 1, 22, 11, 14, 1, 36, 6, 16, 13, 28])



jump_forward = get_divisor_sums(10 ** 6) # graph of amicable nodes: node_1 = divisor_sums[node_0]
jump_backward = {}
for ind, num in enumerate(jump_forward):
    if num not in jump_backward:
        jump_backward[num] = []
    jump_backward[num].append(ind)

assert(jump_forward[12496] == 14288)
assert(jump_forward[14288] == 15472)
assert(jump_forward[15472] == 14536)
assert(jump_forward[14536] == 14264)
assert(jump_forward[14264] == 12496)

assert(jump_backward[12496] == [9464, 12032, 14264, 15476])
assert(jump_backward[14264] == [14536])
assert(jump_backward[14536] == [15472, 29066])
assert(jump_backward[15472] == [14288])
assert(jump_backward[14288] == [12496, 16312])


memo_chain_length = {}
def recursively_walk_backward(num, seen=[]): # DFS
    if num not in memo_chain_length:
        if num in set(seen):
            #print(seen)
            chain_length = len(seen)
            for node in seen:
                memo_chain_length[node] = chain_length
        else:
            nodes = list(filter(lambda x: x <= 10 ** 6, jump_backward.get(num, [])))
            if len(nodes) == 0:
                memo_chain_length[num] = 0
            else:
                chain_length = max([recursively_walk_backward(node, seen + [num]) for node in nodes])
                memo_chain_length[num] = chain_length
    return memo_chain_length[num]

assert(recursively_walk_backward(14264) == 5)
assert(recursively_walk_backward(220) == 2)



longest_chain_length = 0
longest_chain = []
for num in range(4, 10 ** 6 + 1):
    recursively_walk_backward(num)

max_chain_length = 0
smallest_num = 10 ** 6 + 1
for num, chain_length in memo_chain_length.items():
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        smallest_num = num
    elif chain_length == max_chain_length:
        smallest_num = min(num, smallest_num)

print(smallest_num)
