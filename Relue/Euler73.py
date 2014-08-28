def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


def get_list_len(num):
    count = 0
    for d in range(2, num + 1):
        for n in range(d / 3 + 1, d / 2 + 1):
            if n * 2 != d and gcd(d, n) == 1:
                count += 1
    return count


print get_list_len(12000)
