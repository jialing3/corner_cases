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

    def break_down_wrapper(self, n):
        return self.break_down(n, list(range(1, n)))


sol = Solution()
assert sol.break_down_wrapper(0) == 1
assert sol.break_down_wrapper(1) == 0
assert sol.break_down_wrapper(2) == 1
assert sol.break_down_wrapper(3) == 2
assert sol.break_down_wrapper(4) == 4
assert sol.break_down_wrapper(5) == 6
sol.break_down_wrapper(100) # 190569291
