from collections import defaultdict

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n ** .5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

concat = lambda x, y: int(''.join(str(x) + str(y)))

def concat_check(x, y):
    return all([is_prime(concat(x, y)), is_prime(concat(y, x))])

nrange = 1e2
nrange_new=1e4 # guaranteed as 1e4*5 > 26033
lst = range(2, int(nrange))
prime_lst = list(set(lst).difference([x * y for x in lst for y in lst if x * y <= max(lst)]))
prime_lst += [x for x in range(int(nrange), int(nrange_new) + 1) if is_prime(x)]

prime_pair = defaultdict(list)
for x in prime_lst:
    for y in prime_lst:
        if y > x and concat_check(x, y):
            prime_pair[x].append(y)

lst_of_five = []
for key1 in sorted(prime_pair):
    new_lst1 = prime_pair[key1]
    if len(new_lst1) >= 4:
        for key2 in new_lst1:
            new_lst2 = set(new_lst1) & set(prime_pair[key2])
            if len(new_lst2) >= 3:
                for key3 in sorted(new_lst2):
                    new_lst3 = new_lst2 & set(prime_pair[key3])
                    if len(new_lst3) >= 2:
                        for key4 in sorted(new_lst3):
                            new_lst4 = new_lst3 & set(prime_pair[key4])
                            if len(new_lst4) >= 1:
                                lst_of_five.append( [key1, key2, key3, key4, min(new_lst4)] )






