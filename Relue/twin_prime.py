from math import sqrt, ceil
import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

ceiling = 10000000
print 'done'
prime_list = primesfrom2to(3 * ceiling + 1)
twin_prime_list = [(x, prime_list[ind+1]) for ind, x in enumerate(prime_list[:-1]) if prime_list[ind+1]-x==2]

initial = 10
with open('prime_number_ratio_to_n.tsv', 'wb') as f:
    for n in range(3, ceiling + 1):
        lower, upper = n, 3 * n
        for a, b in twin_prime_list:
           if a >= lower and b <= upper:
               break
        else:
           print n, 'found'

        if n > initial:
            print initial
            initial *= 10
            
