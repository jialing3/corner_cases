from math import sqrt

def cycle(n, print_flg=0):
    count = 0
    a, b, c = int(sqrt(n)), 1, int(sqrt(n))
    d = []
    rep = set()
    while True:
        if print_flg:
            print a, ',', b,'/ ( sqrt(', n, ') -', c, ')'
        d.append((a,b,c))
        expression = b / (sqrt(n) - c)
        a = int(expression)
        b = (n - c ** 2) / b   
        c = b * a - c
        if (a,b,c) in d[:-1]:
            initial_ind = d.index((a,b,c))
            if (a,b,c) in d[initial_ind+1:]:
                cycle_length = d.index((a,b,c), initial_ind + 1) - initial_ind
                if d[initial_ind:initial_ind+cycle_length+1] == d[initial_ind+cycle_length:initial_ind+2*cycle_length+1]:
                    return cycle_length
        count += 1
    print n, d

def euler64():
    counter = 0
    for i in range(2, 10001):
        if not sqrt(i).is_integer():
            counter += (cycle(i) % 2)
            #print i
    print counter

def play():
    list1 = []
    for i in range(2, 300):
        if not sqrt(i).is_integer():
            if cycle(i) % 2:
                if not sqrt(i-1).is_integer():
                    list1.append(i)
    print list1

def test1():
    set1 = set()
    list1 = [i**2+1 for i in range(1,1000)]
    for i in range(len(list1)-1):
        for j in range(i):
            if not list1[i] % list1[j] and not sqrt(list1[i] / list1[j]).is_integer():
                set1.add(list1[i] / list1[j])
                #set1.add((list1[i] / list1[j], list1[i], list1[j]))
    set1 = set1 - set(list1)# - set(test2())
    print sorted(set1)[:30]

def test2():
    set1 = set()
    list1 = [i**2+1 for i in range(1,100)]
    for i in range(len(list1)-1):
        for j in range(i):
            set1.add(list1[i] * list1[j])
            #set1.add((list1[i] * list1[j], list1[i], list1[j]))
    set1 = set1 - set(list1)
    return sorted(set1)[:30]

#1 2 1 2 4 2 1 2 2 5, 10000

        #b_tmp = 23 - c ** 2
        #b = b_tmp / b if b_tmp % b == 0 else b_tmp     


#4 , 1 / (sqrt(23) - 4)

#    = (sqrt(23) + 4) / 7

#    = 1 + (sqrt(23) - 3) / 7

#1, 7 / (sqrt(23) - 3)

#    = 7 * (sqrt(23) + 3) / 14

#    = (sqrt(23) + 3) / 2

#    = 3 + (sqrt(23) - 3) / 2

#3, 2 / (sqrt(23) - 3)

#    = 2 * (sqrt(23) + 3) / 14

#    = (sqrt(23) + 3) / 7

#    = 1 + (sqrt(23) - 4) / 7

#1, 7 / (sqrt(23) - 4)

#    = 7 * (sqrt(23) + 4) / 7

#    = (sqrt(23) + 4)

#    = 8 + (sqrt(23) - 8)

#8, 1 / (sqrt(23) - 8)

'''
sqrt(2) = 1 + sqrt(2) - 1
1, 1 / (sqrt(2) - 1)
   = (sqrt(2) + 1) / 1
   = 2 + (sqrt(2) - 1) / 1
2, 1 / (sqrt(2) - 1)
   = (sqrt(2) + 1) / 1
   = 2 + (sqrt(2) - 1) / 1

sqrt(3) = 1 + sqrt(3) - 1
1, 1 / (sqrt(3) - 1)
   = (sqrt(3) + 1) / 2
   = 1 + (sqrt(3) - 1) / 2
1, 2 / (sqrt(3) - 1)
   = 2 * (sqrt(3) + 1) / 2
   = sqrt(3) + 1
   = 2 + (sqrt(3) - 1)
2, 1 / (sqrt(3) - 1)
   = (sqrt(3) + 1) / 2

sqrt(7) = 2 + sqrt(7) - 2
2, 1 / (sqrt(7) - 2)
   = (sqrt(7) + 2) / 3
   = 1 + (sqrt(7) - 1) / 3
1, 3 / (sqrt(7) - 1)
   = 3 * (sqrt(7) + 1) / 6
   = (sqrt(7) + 1) / 2
   = 1 + (sqrt(7) - 1) / 2
1, 2 / (sqrt(7) - 1)
   = 2 * (sqrt(7) + 1) / 6
   = (sqrt(7) + 1) / 3
   = 1 + (sqrt(7) - 2) / 3
1, 3 / (sqrt(7) - 2)
   = 3 * (sqrt(7) + 2) / 3
   = sqrt(7) + 2
   = 4 + (sqrt(7) - 2)
4, 1 / (sqrt(7) - 2)
1
1
1
4

'''
