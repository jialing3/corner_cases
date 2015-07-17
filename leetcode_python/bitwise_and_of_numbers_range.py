class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        #if m == n:
        #    return m

        # get the leading digit
        i = -1
        while 2 ** (i + 1) <= n:
            i += 1

        ans = 0
        while i >= 0:
            if n >= 2 ** i:
                if m >= 2 ** i:
                    ans += 2 ** i
                n -= 2 ** i
                m -= 2 ** i
            i -= 1
        return ans
