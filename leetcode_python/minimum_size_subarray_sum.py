# O(n log n) would be to sort it

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        counter = 0
        while s > 0 and nums:
            running_max = max(nums)
            nums.remove(running_max)
            s -= running_max
            counter += 1
            #print running_max, s
        return counter if s <= 0 else 0
