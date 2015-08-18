# 0 will make everything 0
# two negative numbers will make the result positive


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        current_max, current_min, global_max = 1, 1, None
        for n in nums:
            current_max, current_min = max(current_max * n, current_min * n, n), min(current_max * n, current_min * n, n)
            if global_max is None or global_max < current_max:
                global_max = current_max
        return global_max

