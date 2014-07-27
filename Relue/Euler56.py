def digitSum(a, b):
    return sum(int(x) for x in list(str(a ** b)))

print max((digitSum(a, b), a, b) for a in range(1, 100) for b in range(1, 100))
