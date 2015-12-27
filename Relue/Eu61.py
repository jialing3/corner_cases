triangle = lambda n: n*(n+1)/2
square = lambda n: n**2
pentagonal = lambda n: n*(3*n-1)/2
hexagonal = lambda n: n*(2*n-1)
heptagonal = lambda n: n*(5*n-3)/2
octagonal = lambda n: n*(3*n-2)

digit_split = lambda num: (num / 100, num % 100)

list3 = [digit_split(triangle(x)) for x in range(45, 141)]
list4 = [digit_split(square(x)) for x in range(32, 100)]
list5 = [digit_split(pentagonal(x)) for x in range(26, 82)]
list6 = [digit_split(hexagonal(x)) for x in range(23, 71)]
list7 = [digit_split(heptagonal(x)) for x in range(21, 64)]
list8 = [digit_split(octagonal(x)) for x in range(19, 59)]

AB_3, CD_3 = set([x[0] for x in list3]), set([x[1] for x in list3])
AB_4, CD_4 = set([x[0] for x in list4]), set([x[1] for x in list4])
AB_5, CD_5 = set([x[0] for x in list5]), set([x[1] for x in list5])
AB_6, CD_6 = set([x[0] for x in list6]), set([x[1] for x in list6])
AB_7, CD_7 = set([x[0] for x in list7]), set([x[1] for x in list7])
AB_8, CD_8 = set([x[0] for x in list8]), set([x[1] for x in list8])

def intersect_join(s1, s2, s3, s4, s5, s6):
    return s1 & (s2 | s3 | s4 | s5 | s6)
AB_3 = intersect_join(AB_3, CD_4, CD_5, CD_6, CD_7, CD_8)
CD_3 = intersect_join(CD_3, AB_4, AB_5, AB_6, AB_7, AB_8)
AB_4 = intersect_join(AB_4, CD_3, CD_5, CD_6, CD_7, CD_8)
CD_4 = intersect_join(CD_4, AB_3, AB_5, AB_6, AB_7, AB_8)
AB_5 = intersect_join(AB_5, CD_4, CD_3, CD_6, CD_7, CD_8)
CD_5 = intersect_join(CD_5, AB_4, AB_3, AB_6, AB_7, AB_8)
AB_6 = intersect_join(AB_6, CD_4, CD_5, CD_3, CD_7, CD_8)
CD_6 = intersect_join(CD_6, AB_4, AB_5, AB_3, AB_7, AB_8)
AB_7 = intersect_join(AB_7, CD_4, CD_5, CD_6, CD_3, CD_8)
CD_7 = intersect_join(CD_7, AB_4, AB_5, AB_6, AB_3, AB_8)
AB_8 = intersect_join(AB_8, CD_4, CD_5, CD_6, CD_7, CD_3)
CD_8 = intersect_join(CD_8, AB_4, AB_5, AB_6, AB_7, AB_3)

list3 = [x for x in list3 if x[0] in AB_3 and x[1] in CD_3]
list4 = [x for x in list4 if x[0] in AB_4 and x[1] in CD_4]
list5 = [x for x in list5 if x[0] in AB_5 and x[1] in CD_5]
list6 = [x for x in list6 if x[0] in AB_6 and x[1] in CD_6]
list7 = [x for x in list7 if x[0] in AB_7 and x[1] in CD_7]
list8 = [x for x in list8 if x[0] in AB_8 and x[1] in CD_8]

ans = []
for ind1, lst1 in enumerate([list3, list4, list5, list6, list7, list8]):
    ind_list = [3, 4, 5, 6, 7, 8]
    list_used = set([3, 4, 5, 6, 7, 8])
    for AB1, CD1 in lst1:
        list_used = list_used ^ set([8])
        for ind2, lst2 in enumerate([list3, list4, list5, list6, list7, list8]):
            if ind1 != ind2:
                for AB2, CD2 in lst2:
                    if CD1 == AB2:
                        list_used = list_used ^ set([ind_list[ind2]])
                        for ind3, lst3 in enumerate([list3, list4, list5, list6, list7, list8]):
                            if ind1 != ind3 and ind2 != ind3:
                                for AB3, CD3 in lst3:
                                    if CD2 == AB3:
                                        list_used = list_used ^ set([ind_list[ind3]])
                                        for ind4, lst4 in enumerate([list3, list4, list5, list6, list7, list8]):
                                            if ind1 != ind4 and ind2 != ind4 and ind3 != ind4:
                                                for AB4, CD4 in lst4:
                                                    if CD3 == AB4:
                                                        list_used = list_used ^ set([ind_list[ind4]])
                                                        for ind5, lst5 in enumerate([list3, list4, list5, list6, list7, list8]):
                                                            if ind1 != ind5 and ind2 != ind5 and ind3 != ind5 and ind4 != ind5:
                                                                for AB5, CD5 in lst5:
                                                                    if CD4 == AB5:
                                                                        list_used = list_used ^ set([ind_list[ind5]])
                                                                        for ind6, lst6 in enumerate([list3, list4, list5, list6, list7, list8]):
                                                                            if ind1 != ind6 and ind2 != ind6 and ind3 != ind6 and ind4 != ind6 and ind5 != ind6:
                                                                                for AB6, CD6 in lst6:
                                                                                    if CD5 == AB6 and CD6 == AB1:
                                                                                        list_used = list_used ^ set([ind_list[ind6]])                                     
                                                                                        ans.append( [AB1*100+CD1, ind_list[ind1], AB2*100+CD2, ind_list[ind2], AB3*100+CD3, ind_list[ind3], AB4*100+CD4, ind_list[ind4], AB5*100+CD5, ind_list[ind5], AB6*100+CD6, ind_list[ind6]])

from random import randint
def recurse(whole_lst=[list3, list4, list5, list6, list7, list8], inds=[3, 4, 5, 6, 7, 8], CD_old=None, AB_new=None):
    if len(inds) > 1 and CD_old is None:
        for tmp_ind in range(len(inds)):
            inds2 = inds[:]
            whole_lst2 = whole_lst[:]
            ind = inds2.pop(tmp_ind)
            lst = whole_lst2.pop(tmp_ind)
            for AB, CD in lst:
                AB_new = AB
                tmp = recurse(whole_lst2, inds2, CD, AB_new)
                if tmp:
                    return tmp + [AB*100+CD, ind]
    elif len(inds) > 1 and CD_old is not None:
        for tmp_ind in range(len(inds)):
            inds2 = inds[:]
            whole_lst2 = whole_lst[:]
            ind = inds2.pop(tmp_ind)
            lst = whole_lst2.pop(tmp_ind)
            for AB, CD in lst:
                if CD_old == AB:
                    tmp = recurse(whole_lst2, inds2, CD, AB_new)
                    if tmp:
                        return tmp + [AB*100+CD, ind]
    elif len(inds) == 1:
        ind = inds[0]
        lst = whole_lst[0]
        for AB, CD in lst:
            if CD_old == AB and CD == AB_new:
                return [AB*100+CD, ind]

print recurse()






