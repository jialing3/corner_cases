class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 1:
            return 0

        is_prime = [True if _ % 2 else False for _ in range(n)] # up to less than n
        is_prime[1] = False # 1 is not a prime number

        if n > 2:
            is_prime[2] = True # 2 is a prime number

        sqrt_n = int(n ** .5)
        for i in range(3, sqrt_n + 1, 2):
            if not is_prime[i]: # skip the non-primes
                continue
            else:
                for j in range(i ** 2, n, i):
                    is_prime[j] = False

        return sum(is_prime)
