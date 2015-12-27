# find the integer with the most number of distinct prime factors
# multiple 2, 3, 5, 7, 11, etc, till the product hits 1 million
# need a prime number generator first

numbers = set(range(2, 1001))
for x in range(2, 1001):
    for y in range(2, 1001):
        if x * y in numbers:
            numbers.remove(x * y)

numbers_iter = iter(numbers)
prod = 1

while True:
    try:
        prod *= numbers_iter.next()
        if prod <= 1000000:
            print prod
        else:
            break
    except StopIteration as e:
        break
