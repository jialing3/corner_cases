from math import gcd

nums = []
with open('p099_base_exp.txt') as f:
    for row in f.readlines():
        base, exponent = row.strip().split(',')
        nums.append([int(base), int(exponent)])

def compare_nums(num_0, num_1):
    base_0, exp_0 = num_0
    base_1, exp_1 = num_1
    if base_0 > base_1 and exp_0 > exp_1:
        return 1
    elif base_0 < base_1 and exp_0 < exp_1:
        return -1
    elif base_0 == base_1:
        return 1 if exp_0 > exp_1 else -1 if exp_0 < exp_1 else 0
    elif exp_0 == exp_1:
        return 1 if base_0 > base_1 else -1 # 0 is covered
    else:
        flipped = False
        if base_0 < base_1: # make sure base_0 > base_1 and exp_0 < exp_1
            base_0, base_1 = base_1, base_0
            exp_0, exp_1 = exp_1, exp_0
            flipped = True
        # base_0 ** exp_0 ?? base_1 ** exp_1
        # (base_0 / base_1) ** exp_0 ?? base_1 ** (exp_1 - exp_0)
        # (base_0 / base_1) ** (exp_0 / (exp_1 - exp_0)) ?? base_1
        left = (base_0 / base_1) ** (exp_0 / (exp_1 - exp_0))
        right = base_1
        #print(left, right)
        if left > right:
            return 1 if not flipped else -1
        elif right > left:
            return -1 if not flipped else 1
        else:
            return 0

assert(compare_nums(nums[0], nums[1]) == -1)
max_num = nums[1]
max_line = 1 # 0-based
for ind, num in enumerate(nums):
    if compare_nums(max_num, num) == -1:
        #print(ind, num)
        max_num = num
        max_line = ind

print(max_line + 1)
