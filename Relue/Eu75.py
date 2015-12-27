def get_a_b_c(L):
    answer_set = set()
    for c in range(L / 3 + 1, L / 2):
        for b in range(c / 2 + 1, c):
            a = L - c - b
            if a <= b and a ** 2 + b ** 2 == c ** 2:
                answer_set.add((a, b, c))
    return answer_set


count = 0
for L in range(1, 1500001):
    if len(get_a_b_c(L)) == 1:
        count += 1

print count
