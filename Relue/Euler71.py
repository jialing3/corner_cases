# for each d, find the maximum n that is smaller than 3/7, via division
# among these 1,000,000 n/d combos, find the max
# O(1 million) running time

# n/d < 3/7
# n < d*3/7

# compare for n1 < d1*3/7 and n2 < d2*3/7
# hard to tell from here

# get a couple of test cases to see first

def get_max_n(d):
    return int(d * 3. / 7)

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


fractions = [(get_max_n(d), d) for d in range(1, 1000000)]


for ind, (n, d) in enumerate(fractions):
    gcd_n_d = gcd(n, d)
    if gcd_n_d != 1:
        fractions[ind] = (n / gcd_n_d, d / gcd_n_d)


fractions = list(set(fractions))


fractions.sort(key=lambda x: 1. * x[0] / x[1], reverse=True)

print fractions[:10]
