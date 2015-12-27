def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g


def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


factorial = memoize(factorial) # memoized version of factorial


sum_of_factorial_of_digits = lambda number: sum(factorial(int(digit)) for digit in str(number))


def generator_sum_of_factorial_of_digits(number):
    while True:
        number = sum_of_factorial_of_digits(number)
        yield number


def find_number_of_non_repeating_terms(number):
    g = generator_sum_of_factorial_of_digits(number)
    number_set = set([number])
    while True:
        try:
            next_number = g.next()
            if next_number not in number_set:
                number_set.add(next_number)
            else:
                return len(number_set)
        except StopIteration:
            return len(number_set)
            break
    return


if __name__ == '__main__':
    count = 0
    for i in range(10 ** 6):
        if find_number_of_non_repeating_terms(i) == 60:
            count += 1
    print count
