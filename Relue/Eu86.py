from math import sqrt

'''
x = 6
y = 5
z = 3

# 0 <= a <= x
dist1 = sqrt((x - a) ** 2 + y ** 2) + sqrt(a ** 2 + z ** 2)
# d/da dist1 == 0
a = z * x / (z + y)
x - a = x * y / (z + y)
sqrt((x - a) ** 2 + y ** 2) = y / (z + y) * sqrt((z + y) ** 2 + x ** 2)
sqrt(a ** 2 + z ** 2) = z / (z + y) * sqrt( x ** 2 + (z + y) ** 2)
dist1 = sqrt((z + y) ** 2 + x ** 2)

# 0 <= a <= y
dist2 = sqrt((y - a) ** 2 + x ** 2) + sqrt(a ** 2 + z ** 2)
# d/da dist2 == 0
a = z * y / (z + x)
dist2 = sqrt((z + x) ** 2 + y ** 2)

# dist2 ** 2 - dist1 ** 2 = 2 * z * (x - y) > 0

# 0 <= a <= z
dist3 = sqrt((z - a) ** 2 + y ** 2) + sqrt(a ** 2 + x ** 2)
# d/da dist3 == 0
a = x * z / (x + y)
dist3 =  sqrt((x + y) ** 2 + z ** 2)

# dist3 ** 2 - dist2 ** 2 = 2 * x * (y - z) > 0

start with z <= y <= x
first, build a list of perfect square's
a ** 2 + b ** 2 = c ** 2 with a <= b < c
then either 1) z + y = a, x = b
         or 2) z + y = b, x = a
'''

def perfect_squares_sieve2(limit):
    root2 = 2 ** 0.5
    a = set()
    for i in range(3, limit + 1):
        for j in range(int(i / root2) + 1, i):
            k = int((i ** 2 - j ** 2) ** 0.5)
            if (k, j) not in a:
                if k ** 2 + j ** 2 == i ** 2:
                    a.add((k, j))
                    for l in range(2, limit // i + 1):
                        a.add((k * l, j * l))
    return a

perfect_squares = perfect_squares_sieve2(5000)

'''
perfect_squares = {(3, 4): 5}
for c in range(1, 2000):
    for b in range(1, c):
        for a in range(1, b + 1):
            if a ** 2 + b ** 2 == c ** 2:
                perfect_squares[(a, b)] = c
'''

def count_of_cuboids_given_M(M, c=set()):
    for x in range(1, M + 1):
        for y in range(1, x + 1):
            for z in range(1, y + 1):
                if (x, y, z) not in c:
                    a = z + y
                    b = x
                    if (a, b) in perfect_squares:
                        for d in range(1, M // x + 1):
                            c.add((x * d, y * d, z * d))
                    a = x
                    b = z + y
                    if (a, b) in perfect_squares:
                        for d in range(1, M // x + 1):
                            c.add((x * d, y * d, z * d))
        l = len(list(filter(lambda k: k[0] <= x, c)))
        if l > 1000000:
            print(x, l)
            break
        if x % 100 == 0:
            print(x, l)
    return c

c = count_of_cuboids_given_M(99, c=set())
assert(len(c) == 1975)
c = count_of_cuboids_given_M(100, c=c)
assert(len(c) == 2060)

'''
# determine the upper-bound of the perfect_squares to calculate
c = set()
i = 1
i2o = {}
while i < 101:
    c = count_of_cuboids_given_M(i, c)
    i2o[i] = len(c)
    i += 1

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log2(x[2:]), np.log2(y[2:]))
print(slope, intercept, r_value**2, p_value, std_err)

# np.log2(y) = intercept + slope * np.log2(x)
# np.log2(1M) = 20
# x = 2 ** 11 = 2K
plt.plot(np.log2(x), np.log2(y), '.', np.log2(x), intercept + slope * np.log2(x), '.'); plt.show()
'''

i = 5000
c = count_of_cuboids_given_M(i, set())

# needs further optimization https://en.wikipedia.org/wiki/Pythagorean_triple
