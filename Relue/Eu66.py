D = range(1000 + 1)
for x in xrange(int(1000 ** .5) + 1):
    D.pop(x ** 2 - x)

def solve_x_y(d):
    x, y = 1, 0
    k, m = 1, 1
    while k != 1 or y == 0:
        m = (m + int(d ** .5)) / k * k - m # minimize abs(m*m - d); k divides m, so that x and y are integers
        x, y = long((m * x + d * y) / abs(k)), long((m * y + x) / abs(k))
        k = (m ** 2 - d) / k
    return x, y
                
solutions = []
for d in D:
    solutions.append((solve_x_y(d)[0], d))
print max(solutions)[1]
print

print solutions[:7]
