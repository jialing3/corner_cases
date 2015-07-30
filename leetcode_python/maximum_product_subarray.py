# 0 will make everything 0
# two negative numbers will make the result positive


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        current_max, current_min, global_max = 1, 1, None
        for n in nums:
            current_max, current_min = max(max(n * current_max, n * current_min), n), min(min(n * current_max, n * current_min), n) # at every new number, decide to include the current number in the previous interval or start a new interval
            if global_max:
                global_max = max(global_max, current_max) # current_max is a running max prod for the current interval
            else:
                global_max = current_max
        return global_max
