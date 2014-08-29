class Solution:
    # @return a list of integers
    def grayCode(self, n):
        return [(i >> 1) ^ i for i in range(1 << n)] # right-shift by 1 bit, xor with self
