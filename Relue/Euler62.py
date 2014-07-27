from collections import defaultdict

lexical_order = lambda x: ''.join(sorted(str(x)))
d = defaultdict(list)

def cube_permute_search(n_start=5, n_len=1000):
    cube_lst = map(lambda x: x**3, range(n_start, n_start+n_len))
    for num in cube_lst:
        lex_map = lexical_order(num)
        if len(d[lex_map]) < 4:
            d[lex_map].append(num)
        else:
            return d[lex_map] + [num]
    n_start += n_len
    return cube_permute_search(n_start)

#cube_test = lambda x: round(x**(1./3))**3==x
