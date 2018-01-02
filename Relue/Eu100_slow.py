from math import gcd

def how_many_blue(total):
    # total * (total - 1) == 2 * blue * (blue - 1)
    # 2 * blue ** 2 - 2 * blue - (total ** 2 - total) == 0
    # [-b +/- (b ^ 2 - 4ac)] / 2a
    # blue = [2 +/- (4 + 8(total ^ 2 - total)) ** 0.5] / 4
    delta = (4 + 8 * (total ** 2 - total)) ** 0.5
    blue = (2 + delta) / 4
    if blue % 1 == 0:
        blue = int(blue)
        gcd_0 = gcd(blue, total)
        gcd_1 = gcd(blue - 1, total - 1)
        top = blue // gcd_0 * (blue - 1) // gcd_1
        bottom = total // gcd_0 * (total - 1) // gcd_1
        if bottom == 2 * top:
            return blue
    return None


assert(how_many_blue(21) == 15)
assert(how_many_blue(120) == 85)
assert(how_many_blue(1000000002604) is None)

total = 10 ** 12
while True:
    blue = how_many_blue(total)
    if blue:
        print(blue, total)
        break
    else:
        total += 1
