# find the smallest missing positive integer
# skip if nums[i] < 1 or nums[i] > n
# skip if nums[i] == i + 1
# swap nums[i] with nums[nums[i] - 1], if nums[i] != i + 1, unless nums[i] == nums[nums[i] - 1] (skip)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        ind = 0
        while ind < n:
            x = nums[ind]
            if x < 1 or x > n:
                ind += 1
            elif x == ind + 1:
                ind += 1
            else:
                if nums[x - 1] == x:
                    ind += 1
                else:
                    nums[ind], nums[x - 1] = nums[x - 1], nums[ind]

        # if x is in nums, it will be at position ind + 1
        for ind, x in enumerate(nums):
            if x != ind + 1:
                return ind + 1
        return n + 1
