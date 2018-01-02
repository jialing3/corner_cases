
# total * (total - 1) == 2 * blue * (blue - 1)
# total or total - 1 needs to be divisible by 4

total = 10 ** 12
blue = 707106781186
tmp = total * (total - 1) - 2 * blue * (blue - 1)
while tmp != 0:
    #print(tmp)
    if tmp > 0:
        blue += 1
        tmp -= 4 * (blue - 1)
    else:
        total += 1
        tmp += 2 * (total - 1)
        if total % 4 not in (0, 1):
            total += 1
            tmp += 2 * (total - 1)
print(blue, total)
