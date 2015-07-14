# edge case: one house

# if 0th house gets robbed, then -1 th house doesn't
# vice versa
# to turn this problem back into the original linear (non-circular) problem

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        max_previous = nums[0]
        max_current = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            max_previous, max_current = max_current, max(max_previous + nums[i], max_current)
        max_left = max_current

        max_previous = nums[-1]
        max_current = max(nums[-1], nums[0])
        for i in range(1, len(nums) - 2):
            max_previous, max_current = max_current, max(max_previous + nums[i], max_current)
        max_right = max_current

        return max(max_left, max_right)
            
