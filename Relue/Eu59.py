# ord(), chr()

f = [int(x) for x in open('cipher1.txt').readline().strip().split(',')]

start = ord('a')
end = ord('z')

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            a = (i, j, k)
            lst = ''.join([chr(x^a[ind % 3])  for ind, x in enumerate(f)])
            if ' the ' in lst.lower():
                print sum([ord(x) for x in lst])
                print lst
