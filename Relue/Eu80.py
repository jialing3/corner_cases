# need digit-by-digit method to get to 100-digit precision
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

def root(n, tol=1e-100):
    if type(n) != int:
        return -1
    else:
        test = 1
        while abs(test ** 2 - n) > tol:
            new_test = (test + n / test) / 2
            if abs(new_test - test) <= tol:
                test = new_test
                break
            else:
                test = new_test
        return test

assert root(16) == 4


def digit_by_digit_root(n, num_digits=100):
    c = n
    p = 0
    for _ in range(num_digits - 1):
        c *= 100
        x = (c // 20 // p) if p != 0 else 1
        while x * (20 * p + x) <= c:
            x += 1
        x -= 1

        c -= x * (20 * p + x)
        p = 10 * p + x

        if c == 0:
            return p // 10
    return p

assert sum(map(int, str(digit_by_digit_root(2)))) == 475
assert digit_by_digit_root(4) == 2

result = 0
for i in range(1, 100):
    curr_root = digit_by_digit_root(i)
    if len(str(curr_root)) < 100:
        continue
    result += sum(map(int, str(curr_root)))

print(result)
