class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        for exponent in range(32, 0, -1):
            divisor = 2 ** exponent
            if n >= divisor:
                cnt += 1
                n %= divisor
        return cnt + n

    def hammingWeight_fast(self, n):
        cnt = 0
        while n != 0:
            n = n & n - 1
            cnt += 1
        return cnt
