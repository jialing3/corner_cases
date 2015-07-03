# no, it does not affect the run-time complexity.
# if the array stays flat all the way to the end, the first element is still the minimum.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]
