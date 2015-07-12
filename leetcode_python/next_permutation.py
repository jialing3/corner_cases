class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) <= 1:
            return

        # if last two are acsending, swap is sufficient
        if nums[-2] < nums[-1]:
            nums[-2], nums[-1] = nums[-1], nums[-2]
        # if last two are non-ascending, need to find out to which digit the non-ascending pattern persists and push up the precedent digit
        else:
            n = len(nums) - 2
            while n > 0 and nums[n - 1] >= nums[n]:
                n -= 1
            # switch the precedent digit with the next largest number
            if n > 0:
                m = len(nums) - 1
                while m > n - 1 and nums[m] <= nums[n-1]:
                    m -= 1
                nums[m], nums[n - 1] = nums[n - 1], nums[m]
            # turn non-ascending into ascending
            nums[n:] = reversed(nums[n:])
