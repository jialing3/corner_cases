class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        length = len(num)
        min_diff = float('inf')
        for i, a in enumerate(num):
            j, k = i + 1, length - 1
            while j < k:
                b, c = num[j], num[k]
                diff = target - (a + b + c) # can be positive or negative
                if diff >= abs(min_diff): # sum too small
                    j += 1
                elif diff <= -abs(min_diff): # sum too large
                    k -= 1
                else: # -min_abs_diff < diff < min_abs_diff
                    min_diff = diff
                    if diff >= 0:
                        j += 1
                    else:
                        k -= 1
        return target - min_diff
                
