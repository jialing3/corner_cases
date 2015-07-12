class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        members = set(nums)
        max_length = 1
        for x in nums:
            if x in members:
                k = 1
                while x + k in members:
                    members.remove(x + k)
                    k += 1
                l = 1
                while x - l in members:
                    members.remove(x - l)
                    l += 1
                if k + l - 1 > max_length:
                    max_length = k + l - 1
                if k > 1 or l > 1:
                    members.remove(x)
        return max_length
                
