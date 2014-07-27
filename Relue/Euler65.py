def first_n_convergent(n, seq):
    current = [0, 1]
    for x in reversed(seq[:n]):
        current = [current[1], current[1] * x + current[0]]
    return (current[1], current[0])

print first_n_convergent(10, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2])

#   2 + 0 / 1
# = 1 / [(2 * 1 + 0) / 1]

new_seq = [2]
for i in range(33):
    new_seq.extend([1, 2 * (i + 1), 1])
bla = first_n_convergent(100, new_seq)
sum(int(x) for x in list(str(bla[0])))
