# k <= N[k] <= 2k
# k = 1 + 1 + ... + 1
# 2k = 2 * k = 2 + k + 1 + ... + 1

from functools import reduce
import numpy as np

def get_prod_and_sum(lst, memo):
    lst = tuple(sorted(lst))
    if tuple(lst) not in memo:
        if len(lst) == 2:
            a, b = lst
            memo[lst] = (a * b, a + b)
        else:
            head, tail = lst[:-1], lst[-1]
            prev_prod, prev_sum = get_prod_and_sum(head, memo)
            memo[lst] = (prev_prod * tail, prev_sum + tail)
    return memo[lst]

def update_N(lst, N, memo):
    __prod__, __sum__ = get_prod_and_sum(lst, memo)
    diff_in_prod_and_sum = __prod__ - __sum__
    k = diff_in_prod_and_sum + len(lst)
    if k <= 12000 and N[k] > __prod__:
        N[k] = __prod__
    return

def grow_tree_to_curr_num(curr_num, N, memo):
    memo_keys = list(memo.keys())
    for head_lst in memo_keys:
        upper_bound = int(np.log(24000 / memo[head_lst][0]) / np.log(curr_num)) + 1 # N[k] <= 2k
        for j in range(1, upper_bound):
            tail_lst = [curr_num for _ in range(j)]
            update_N(list(head_lst) + tail_lst, N, memo)

N = [np.Inf for _ in range(12001)]
N[0] = 0
N[1] = 0
memo = {(): (1, 0)} # ideally, memo should be a Trie

curr_num = 2
num_unfilled = len(list(filter(lambda x: x is np.Inf, N)))
while num_unfilled > 0:
    grow_tree_to_curr_num(curr_num, N, memo)
    num_unfilled = len(list(filter(lambda x: x is np.Inf, N)))
    print(curr_num, num_unfilled)
    curr_num += 1


assert(N[:13] == [0, 0, 4, 6, 8, 8, 12, 12, 12, 15, 16, 16, 16])

print(sum(set(N)))
