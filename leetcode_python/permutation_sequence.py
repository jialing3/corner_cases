# def factorial

# if k == 1, return the remaining numbers in ascending order
# else
#       k // (n-1)! gives the fist number in sequence
#       then set k %= (n-1)!

#       remove the first number in sequence from the remaining numbers, recurse


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self):
        self.memo = {}

    def getPermutation(self, n, k):
        nums = [str(_) for _ in range(1, n + 1)]
        return ''.join(self.recurse(nums, k - 1))


    def recurse(self, nums, k):
        if k == 0:
            return sorted(nums)
        else:
            n = len(nums)
            if k == self.factorial(n) - 1:
                return sorted(nums, reverse=True)
            else:
                n_minus_1_factorial = self.factorial(n - 1)
                ind = k // n_minus_1_factorial
                return [nums[ind]] + self.recurse(nums[:ind] + nums[ind + 1:], k % n_minus_1_factorial)


    def factorial(self, n):
        if n in self.memo:
            return self.memo[n]
        elif n == 1:
            self.memo[1] = 1
            return 1
        else:
            self.memo[n] = n * self.factorial(n - 1)
            return self.memo[n]
