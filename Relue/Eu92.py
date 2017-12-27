

def get_next_in_the_chain(curr):
    next_num = 0
    while curr > 0:
        curr, remainder = divmod(curr, 10)
        next_num += remainder ** 2
    return next_num


assert(get_next_in_the_chain(44) == 32)
assert(get_next_in_the_chain(89) == 145)

def loop(curr, memo):
    seen_in_the_loop = []
    while curr not in (1, 89):
        if curr in memo:
            curr = memo[curr]
        else:
            seen_in_the_loop.append(curr)
            curr = get_next_in_the_chain(curr)
    for num in seen_in_the_loop:
        memo[num] = curr
    return

memo = {1: 1, 89: 89}
loop(44, memo)
loop(85, memo)
loop(145, memo)
assert(memo[44] == 1)
assert(memo[20] == 89)

for curr in range(1, 10 ** 7 + 1):
    loop(curr, memo)

print(len(list(filter(lambda x: x[1] == 89, memo.items()))))
