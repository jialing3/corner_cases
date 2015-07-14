# subsequences of S that match T
# DP

# i-th element in S, j-th element in T
# E(i, j) = (E(i-1, j-1) + E(i-1, j)) * (x[i] == y[j])) + E(i-1, j) * (x[i] != y[j])
# E(0, j) = 0 for j != 0
# E(i, 0) = 1

# '' is a subsequence of any string
# if s[i] == t[j], s[i] can either be included in the subsequence or not
# if s[i] != t[j], s[i] cannot be included in the subsequence

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        e_last = [1] + [0] * n
        for i in range(1, m + 1):
            e_current = [1] + [0] * n
            for j in range(1, n + 1):
                e_current[j] = e_last[j] + (e_last[j - 1] if s[i - 1] == t[j - 1] else 0)
            e_last = e_current[:]
        return e_last[-1]
