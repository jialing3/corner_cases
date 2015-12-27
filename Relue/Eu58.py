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

n=-1
pCnt=0
Cnt=0

while pCnt == 0 or 1. * pCnt / Cnt >= .1:
    n += 2
    if n == 1:
        lst = [1]
        Cnt += 1
    else:
        pCnt += is_prime(n**2 - n*3 + 3) + is_prime(n**2 - n*2 + 2) + is_prime(n**2 - n + 1) # n**2
        Cnt += 4
print pCnt, Cnt, n

    
   
