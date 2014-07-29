class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        sum_2 = {}
        for i, num1 in enumerate(num):
            for j, num2 in enumerate(num):
                if i < j:
                    tmp_sum = num1 + num2
                    if tmp_sum not in sum_2:
                        sum_2[tmp_sum] = {}
                    sum_2[tmp_sum][(i, j)] = [num1, num2]

        solutions = set([])
        for k, num3 in enumerate(num):
            target = 0 - num3
            if target in sum_2:
                for i, j in sum_2[target].keys():
                    if k != i and k != j:
                        solutions.add(tuple(sum_2[target][(i, j)] + [num3]))

        return [list(row) for row in solutions]
