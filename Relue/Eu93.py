from itertools import combinations, permutations

def get_candidate_digit_list():
    return combinations(range(10), 4)

def perform_all_possible_operations(num_0, num_1):
    if num_1 != 0:
        return [num_0 + num_1, num_0 - num_1, num_0 * num_1, num_0 / num_1]
    else:
        return [num_0 + num_1, num_0 - num_1, num_0 * num_1]

def get_possible_targets(num_sequence):
    # a operator b operator c operator d
    curr_list = set([num_sequence[0]])
    for next_num in num_sequence[1:]:
        next_list = set()
        for num in curr_list:
            for result in perform_all_possible_operations(num, next_num):
                next_list.add(result)
        curr_list = next_list.copy()
    target_set = set(map(int, filter(lambda x: x > 0 and x % 1 == 0, curr_list)))
    # a operator (b operator c) operator d
    for middle_num in perform_all_possible_operations(num_sequence[1], num_sequence[2]):
        curr_list = set([num_sequence[0]])
        for next_num in [middle_num, num_sequence[3]]:
            next_list = set()
            for num in curr_list:
                next_list.add(num + next_num)
                next_list.add(num - next_num)
                next_list.add(num * next_num)
                if next_num != 0:
                    next_list.add(num / next_num)
            curr_list = next_list.copy()
        target_set |= set(map(int, filter(lambda x: x > 0 and x % 1 == 0, curr_list)))
    # (a operator b) operator (c operator d)
    curr_list = set()
    for num_0 in perform_all_possible_operations(num_sequence[0], num_sequence[1]):
        for num_1 in perform_all_possible_operations(num_sequence[2], num_sequence[3]):
            for result in perform_all_possible_operations(num_0, num_1):
                curr_list.add(result)
    target_set |= set(map(int, filter(lambda x: x > 0 and x % 1 == 0, curr_list)))
    return target_set

possible_target_set = set()
for num_sequence in permutations([1, 2, 3, 4], 4):
    possible_target_set |= get_possible_targets(num_sequence)

assert(max(possible_target_set) == 36)
assert(all([target in possible_target_set for target in range(1, 29)]))

max_length_of_consecutive_positive_integer_targets = 28
max_combo = '1234'
for combo in get_candidate_digit_list():
    possible_target_set = set()
    for num_sequence in permutations(combo, 4):
        possible_target_set |= get_possible_targets(num_sequence)
    target = 1
    while target in possible_target_set:
        target += 1
    if target - 1 > max_length_of_consecutive_positive_integer_targets:
        max_length_of_consecutive_positive_integer_targets = target - 1
        max_combo = ''.join(map(str, combo))

print(max_combo)
