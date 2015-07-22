class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        if k == 0 or k == n:
            return

        i = 0
        start = 0
        tmp = nums[i]
        cnt = 0
        while True:
            i = (i + k) % n
            tmp, nums[i] = nums[i], tmp
            cnt += 1
            if i == start:
                if cnt < n:
                    start += 1
                    i = start
                    tmp = nums[i]
                else:
                    break
        return
