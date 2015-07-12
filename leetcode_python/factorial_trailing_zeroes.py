class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        total = 0
        while n >= 5:
            total += n / 5
            n /= 5
        return total
