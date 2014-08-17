class Solution:
    # @param n, an integer
    # @return an integer

    cached = {0: 1, 1: 1}

    def climbStairs(self, n):
        if n not in self.cached:
            self.cached[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cached[n]
