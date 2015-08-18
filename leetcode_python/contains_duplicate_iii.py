from collections import OrderedDict

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0 or t < 0:
            return False

        approximation_dict = OrderedDict()
        for i, n in enumerate(nums):
            key = n // (t + 1)
            if (key in approximation_dict and abs(approximation_dict[key] - n) <= t) or (key - 1 in approximation_dict and abs(approximation_dict[key - 1] - n) <= t) or (key + 1 in approximation_dict and abs(approximation_dict[key + 1] - n) <= t):
                return True
            approximation_dict[key] = n
            if i >= k: # i, not len(approximation_dict)
                approximation_dict.popitem(last=False)
        return False
