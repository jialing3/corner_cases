# need digit-by-digit method to get to 100-digit precision
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

def root(n):
    if type(n) != int:
        return -1
    else:
        test = 1
        while abs(test ** 2 - n) > 0.1 ** 100:
            new_test = (test + n / test) / 2
            if abs(new_test - test) < 0.1 ** 100:
                test = new_test
                break
            else:
                test = new_test
        return test

assert root(16) == 4

def digit_by_digit_root(n):
