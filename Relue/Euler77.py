class Solution:
    def __init__(self):
        self.memo = {}

    def break_down(self, n, to_use):
        if type(n) != int or type(to_use) != list:
            return 0
        else:
            if len(to_use) == 0:
                return 1 if n == 0 else 0
            elif len(to_use) == 1 and to_use[0] == n:
                return 1
            elif (n, tuple(to_use)) in self.memo:
                return self.memo[n, tuple(to_use)]
            else:
                not_used = self.break_down(n, to_use[:-1])
                used = self.break_down(n - to_use[-1], list(filter(lambda x: x <= n - to_use[-1], to_use)))
                self.memo[n, tuple(to_use)] = not_used + used
                #print(n, to_use[-1], not_used, used)
                return not_used + used

    def sieve_prime(self, n):
        non_prime = set()
        for i in range(2, n):
            for j in range(2, n):
                non_prime.add(i * j)
        return [x for x in range(1, n + 1) if x not in non_prime]

    def break_down_wrapper(self, n):
        return self.break_down(n, self.sieve_prime(n))


sol = Solution()
assert sol.break_down_wrapper(10) == 5
