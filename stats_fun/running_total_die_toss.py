from pprint import pprint

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

def prob_total_equal_n(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 1. / 6 * sum(prob_total_equal_n(n - i) for i in range(1, 7))

prob_total_equal_n = memoize(prob_total_equal_n)

if __name__ == '__main__':
    pprint([prob_total_equal_n(j) for j in range(30)])
