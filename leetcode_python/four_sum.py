class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        if sum(num[-4:]) < target or sum(num[:4]) > target: # edge case
            return []
        length = len(num)
        if length < 4:
            return []
        solution_set = set()
        for i, a in enumerate(num):
            if a + num[length - 3] + num[length - 2] + num[length - 1] < target:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and num[j] == num[j - 1]:
                    continue
                if a + num[j] + num[length - 2] + num[length - 1] < target:
                    continue
                k, l = j + 1, length - 1
                while k < l:
                    if k > j + 1 and num[k] == num[k - 1]:
                        k += 1
                        continue
                    elif l < length - 1 and num[l] == num[l + 1]:
                        l -= 1
                        continue
                    b, c, d = num[j], num[k], num[l]
                    total = a + b + c + d
                    print a, b, c, d, total
                    if total == target:
                        solution_set.add((a, b, c, d))
                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1
                    else: # total > target
                        l -= 1
        return [list(x) for x in solution_set]
