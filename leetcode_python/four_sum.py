# two sum way

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        count = {}
        for a in num:
            count[a] = count.get(a, 0) + 1
        two_sum = {} # O(n^2) space
        length = len(num)
        for i in range(length):
            for j in range(i + 1, length):
                tmp = num[i] + num[j]
                if tmp not in two_sum:
                    two_sum[tmp] = []
                two_sum[tmp].append((num[i], num[j])) # build a list of tuples
        two_sum_list = sorted(two_sum.keys())
        length_2 = len(two_sum_list)
        i, j = 0, length_2 - 1
        output_list = set()
        while i <= j: # equal sign
            a, b = two_sum_list[i], two_sum_list[j]
            four_sum = a + b
            if four_sum == target:
                for tmp_four in [sorted(c + d) for c in two_sum[a] for d in two_sum[b]]: # what about overlapping elements?
                    output_list.add(tuple(tmp_four))
                i += 1
                j -= 1
            elif four_sum < target:
                i += 1
            else: # four_sum > target
                j -= 1
        for tmp_four in list(output_list):
            tmp_count = {}
            for tmp_one in tmp_four:
                tmp_count[tmp_one] = tmp_count.get(tmp_one, 0) + 1
            for tmp_one, cnt in tmp_count.iteritems():
                if cnt > 1 and cnt > count[tmp_one] and tmp_four in output_list:
                    output_list.remove(tmp_four)
        return [list(x) for x in output_list]
        
