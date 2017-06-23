#!/usr/local/bin/python3
'''
cnt = sum_over_x, sum_over_y (x * y)
    = sum_over_x (x) * sum_over_y (y)
    = [(1 + width) * width / 2] * [(1 + length) * length / 2]
'''

def rect_counter(width, length):
    cnt = 0
    for x in range(1, width + 1):
        for y in range(1, length + 1):
            cnt += x * y
    return cnt


def rect_counter_2(width, length):
    return sum(range(1, width + 1)) * sum(range(1, length + 1))


def rect_counter_3(width, length):
    return (1 + width) * width * (1 + length) * length // 4

print(rect_counter(2, 3))
print(rect_counter_2(2, 3)) # faster
print(rect_counter_3(2, 3)) # fastest


def get_approximate_width(length, cnt):
    a = 1
    b = 1
    c = -cnt * 4 // ((1 + length) * length)
    delta = (b ** 2 - 4 * a * c) ** .5
    return map(int, filter(lambda x: x > 2,
           [(-b + delta) // (2 * a), (-b - delta) // (2 * a)]))


def abs_diff(width, length, cnt):
    return abs(cnt - rect_counter_3(width, length))


def get_width_with_min_cnt(length, cnt):
    d = {}
    for approx_width in get_approximate_width(length, cnt):
        for width in range(approx_width - 3, approx_width + 4):
            d[abs_diff(width, length, cnt)] = width
    min_diff = min(d.keys())
    return d[min_diff], min_diff


cnt = int(2e6)
d = {}
for length in range(1, 55):
    width, min_diff = get_width_with_min_cnt(length, cnt)
    d[min_diff] = [width, length]
min_diff = min(d.keys())
width, length = d[min_diff]
print(width, length, width * length)
