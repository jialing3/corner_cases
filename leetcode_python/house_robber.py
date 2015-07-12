class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        total = [0] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            total[i] = max(total[i - 2] + nums[i], total[i - 1])
        return total[-1]
        
