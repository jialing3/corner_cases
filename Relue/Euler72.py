# Euler's totient function
# muliply the multiples of every prime number by (1-1/p)
# it's like gradually applying the totient function


totient = range(10 ** 6 + 1)

for d in range(2, 10 ** 6 + 1):
    if totient[d] == d: # d is prime
        for multiple in range(d, 10 ** 6 + 1, d):
            totient[multiple] -= totient[multiple] / d

print sum(totient) - 1
