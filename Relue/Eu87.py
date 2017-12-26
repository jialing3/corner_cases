



def yield_prime(limit):
    sieve = [True for _ in range(limit + 1)]
    sieve[0] = sieve[1] = False

    for num, is_prime in enumerate(sieve):
        if is_prime:
            yield num
            for multiplier in range(2, limit // num + 1):
                sieve[multiplier * num] = False

def get_count(limit_squared):
    limit = int(limit_squared ** 0.5)
    primes = list(yield_prime(limit))
    squares = list(filter(lambda x: x < limit_squared, map(lambda x: x ** 2, primes)))
    cubes = list(filter(lambda x: x < limit_squared, map(lambda x: x ** 3, primes)))
    quads = list(filter(lambda x: x < limit_squared, map(lambda x: x ** 4, primes)))

    count = 0
    uniques = set()
    for a in quads:
        for b in cubes:
            for c in squares:
                if a + b + c < limit_squared:
                    #print(int(c ** 0.5), '^ 2 + ', int(b ** (1 / 3)), '^ 3 + ', int(a ** 0.25), '^ 4 = ', a + b + c)
                    count += 1
                    uniques.add(a + b + c)

    print('\n', limit_squared, ': ', count, len(uniques))


get_count(50)
get_count(5000)
get_count(50000000)
