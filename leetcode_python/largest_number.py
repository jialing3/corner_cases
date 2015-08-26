# comparison sort
# comparison criteria is lambda a, b: a + b > b + a

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        nums.sort(cmp = lambda a, b: cmp(a + b, b + a), reverse=True)
        output = ''.join(nums)
        # trim leading '0'
        while len(output) > 1 and output[0] == '0':
            output = output[1:]
        return output
    
