def isPanlidrome(num):
    num = str(num)
    return num[::-1] == num

def addReverse(num):
    rev = int(str(num)[::-1])
    return num + rev

def isLychrel(num):
    counter = 50
    while counter > 0:
        num = addReverse(num)
        if isPanlidrome(num): return False
        counter -= 1
    return True

lst = [x for x in range(1, 10000) if isLychrel(x)]
print len(lst)
print 349, 349 in lst, '\n', 196, 196 in lst, '\n', 4994, 4994 in lst

