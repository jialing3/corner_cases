class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        else:
            return nums[0]
