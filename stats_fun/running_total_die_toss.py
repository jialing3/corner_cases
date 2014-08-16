from pprint import pprint
import matplotlib.pyplot as plt

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
    P_n = [prob_total_equal_n(j) for j in range(100)]
    pprint(P_n)
    plt.plot(range(1, 100), P_n[1:], '.:', alpha=.5) # plateaus at around n = 20
    plt.show()
