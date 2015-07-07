class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        seen = set([n])
        while n != 1:
            n = self.sum_squared_digits(n)
            if n in seen:
                return False
            seen.add(n)
        return True

    def sum_squared_digits(self, n):
        return sum(int(d) ** 2 for d in str(n))
