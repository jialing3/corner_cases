# opposite to the last problem, now we want as few distinct prime number factors as possible
# which will make the ratio of n / phi(n) minimal

# having one prime number factor once is not a good solution,
# as phi(prime_n) = prime_n - 1
# this will fail the permutation criteria

# the solution can be composed of two (not necessarily distinct) prime number factors
# let's consider the distinct case
# phi(prime_n1 * prime_n2) = (prime_n1 - 1) * (prime_n2 - 1)

# for the case with the same prime factor twice
# phi(prime_n ^ 2) = (prime_n - 1) * prime_n
# ratio is very close to 1, too


upper_limit = 2 * int((10 ** 8) ** .5) + 1
prime_numbers = set(range(2, upper_limit)) - set(x * y for x in range(2, upper_limit) for y in range(2, upper_limit))
prime_numbers = sorted(prime_numbers)


def phi(n):
    coprimes = set(range(1, n + 1)) - set(x * y for x in range(2, n + 1) if n % x == 0 for y in range(1, n + 1)) # sieve method
    return len(coprimes)


def is_permutation(n1, n2):
    return sorted(str(n1).replace('0', '')) == sorted(str(n2).replace('0', ''))


ratios = []
phi__ = dict()
for n1 in prime_numbers:
    phi_n1 = phi(n1)
    phi__[n1] = phi_n1
    for n2 in prime_numbers:
        if n2 < n1 and n1 * n2 <= 10 ** 7:
            phi_n2 = phi__[n2]
            if is_permutation(n1 * n2, phi_n1 * phi_n2):
                ratios.append((1. * n1 * n2 / phi_n1 / phi_n2, n1 * n2))
                #print n1 * n2, phi_n1 * phi_n2, 1. * n1 * n2 / phi_n1 / phi_n2


ratios.sort()
print ratios[0][1]
