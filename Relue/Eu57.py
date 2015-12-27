from math import log10
#from fractions import Fraction
#Fraction does not work, have to write own function to convert decimal to fraction
#300 digits
#b = [2 1; 1 0] raised to the n-th power

def root2plus1(n=0, num=2., numerator=2, denominator=1):
    while n < 1000: #1000
        n += 1
        num = 2 + 1 / num
        numerator, denominator = 2 * numerator + denominator, numerator
        yield (n, num - 1, int(log10(numerator - denominator)), int(log10(denominator)))

cnt = 0
for x in root2plus1():
    cnt += x[2] > x[3]
    #print x, x[2] > x[3]
print cnt
