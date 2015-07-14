class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        inds_table = {}
        for ind, num in enumerate(nums):
            if num not in inds_table:
                inds_table[num] = ind
            else:
                if ind - inds_table[num] <= k:
                    return True
                else: # replace the original ind
                    inds_table[num] = ind
        return False
