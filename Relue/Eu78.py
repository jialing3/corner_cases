# not efficient yet
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
                # pre-calculation to prevent recursion error
                for i in range(1, len(to_use) - 2):
                    self.break_down(n, to_use[:i])
                not_used = self.break_down(n, to_use[:-1]) # original recursion error
                used = self.break_down(n - to_use[-1], list(filter(lambda x: x <= n - to_use[-1], to_use)))
                self.memo[n, tuple(to_use)] = not_used + used
                #print(n, to_use[-1], not_used, used)
                return not_used + used

    def break_down_wrapper(self, n):
        return self.break_down(n, list(range(1, n + 1)))

if __name__ == '__main__':
    sol = Solution()
    assert sol.break_down_wrapper(5) == 7

    n = 0
    while True:
        number_of_ways = sol.break_down_wrapper(n)
        #print(n, number_of_ways)
        if number_of_ways % 10 ** 6 == 0:
            break
        n += 1
    print(n, number_of_ways)
