class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        
