# http://mathworld.wolfram.com/PartitionFunctionP.html
# recursive relation
# P(n) = sum((-1) ** (k + 1) * (P[n - 1/2 * k (3k - 1)] + P[n - 1/2 * k (3k + 1)]) for k in range(1, n + 1))
# Hint: Is 7213+12965+40122 divisible by 100? What about 13+65+22?
#       only need to keep the last six digits

class Solution:
    def __init__(self):
        self.p = [0] * 10 ** 5
        self.p[0] = 1
        self.p[1] = 1

    def get_p(self, n):
        if n < 0:
            return 0
        elif self.p[n]:
            return self.p[n]
        else:
            temp_sum = 0
            for k in range(1, n + 1):
                n1 = self.get_p(n - k * (3 * k - 1) // 2)
                n2 = self.get_p(n - k * (3 * k + 1) // 2)
                if k % 2:
                    temp_sum += n1 + n2
                else:
                    temp_sum -= n1 + n2
            self.p[n] = temp_sum % 10 ** 6
            return self.p[n]

    def test(self):
        assert self.get_p(5) == 7


if __name__ == '__main__':
    sol = Solution()
    sol.test()

    n = 5
    while sol.get_p(n):
        n += 1

    print(n)
