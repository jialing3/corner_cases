import numpy as np

D = range(1000 + 1)
for x in xrange(int(1000 ** .5) + 1):
    D.pop(x ** 2 - x)

def solve_x_y(d):
    x = int(np.ceil((1 + d) ** .5))
    #y = int (((x ** 2 - 1.) / d) ** .5)
    y = 1
    while True:
        #print x, y, d
        left = x ** 2 - d * y ** 2
        if left == 1:
            return (x, y)
        elif left > 1:
            y += 1
        else:
            x += 1

solutions = []
for d in D:
    solutions.append((solve_x_y(d)[0], d))
print max(solutions)[1]
