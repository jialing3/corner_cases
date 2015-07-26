class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        # keep two numbers' counts, as there can be at most 2 majority numbers
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0: # num not in (n1, n2), and count for n1 is 0, pick a new n1
                n1, c1 = num, 1
            elif c2 == 0: # count for n2 is 0
                n2, c2 = num, 1
            else: # counts for n1 and n2 are not 0 yet, but num matches neither
            # to balance out 1/3 of the nums, one would need at least 1/3 of other random numbers
            # n1 and n2 are not guaranteed to majority
                c1, c2 = c1 - 1, c2 - 1

        len_nums = len(nums)
        return [n for n in (n1, n2) if n is not None and nums.count(n) > len_nums / 3]
