class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []

        queue = nums[:k]
        output = [max(queue)]

        ind = k
        while ind < len(nums):
            queue = queue[1:] + [nums[ind]]
            output.append(max(queue))
            ind += 1

        return output
        
