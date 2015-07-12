class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return False if n == 0 else (n & (n - 1)) == 0
