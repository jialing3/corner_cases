# Find the last 10 digits of 28433*2**7830457+1

# 2 ^ n is 10 ^ n in base-2
# to convert from base-20 to base-10, just sum individual digits
# 28433(base-10) is 110111100010001(base-2), with '{0:b}'.format(28433)

# 28433*2**7830457(base-10) is 110111100010001(base-2) * ( 10 ^ 7830457 (base-2) )
# 28433*2**7830457+1(base-10) is 110111100010001`000...000`1, with 7830456 0's in ``

# -----------------------------------------------------
# power of 2 mod 10 ** (m - 1)
# can ignore all the components up to 10 ** (m - 1)

def mth_last_digit_of_2_to_the_power_n(n, m): # m is 1-based
    return (2 ** n // 10 ** (m - 1)) % 10

# The last digit of 2 ** n is D[n % 4], where D = {1: 2, 2: 4, 3: 8, 0: 6}
# The last digit of 2**7830457 is __2__, as 57 % 4 == 1

# The second last digit of 2 ** n follows a 20-element-long cycle,
# The second last digit of 2**7830457 is __7__, as 57 % 20 == 17

# The third last digit of 2 ** n follows the pattern of [8, 7, 5, 1, 3, 6, 3, 6, 3, 7, 5, 0, 0, 0, 0, 1, 2, 5, 0, 0, 0, 1, 3, 7, 5, 0, 1, 2, 5, 1, 3, 6, 2, 4, 8, 7, 4, 9, 8, 6, 2, 5, 1, 3, 7, 4, 9, 8, 7, 5, 1, 2, 4, 8, 6, 3, 6, 3, 6, 2, 4, 9, 9, 9, 9, 8, 7, 4, 9, 9, 9, 8, 6, 2, 4, 9, 8, 7, 4, 8, 6, 3, 7, 5, 1, 2, 5, 0, 1, 3, 7, 4, 8, 6, 2, 5, 0, 1, 2, 4]
# with print([mth_last_digit_of_2_to_the_power_n(n, 3) for n in range(300)])
# The cycle length is 100 -- so the jump is 5-fold for each digit
# The third last digit of 2**7830457 is __8__, as 457 % 100 is 57

# 4th last digit:
# [mth_last_digit_of_2_to_the_power_n(n, 4) for n in range(201, 701)] ==
# [mth_last_digit_of_2_to_the_power_n(n, 4) for n in range(701, 1201)]
# 4th last digit of 2**7830457 is __3__, as 457 % 500 is 457

# 5th last digit:
# [mth_last_digit_of_2_to_the_power_n(n, 5) for n in range(201, 2701)] == [mth_last_digit_of_2_to_the_power_n(n, 5) for n in range(2701, 5201)]
# 5th last digit of 2**7830457 is __0__, as 0457 % 2500 is 457

# 6th last digit:
# [mth_last_digit_of_2_to_the_power_n(n, 6) for n in range(201, 12701)] == [mth_last_digit_of_2_to_the_power_n(n, 6) for n in range(12701, 25201)]
# 6th last digit of 2**7830457 is __3__, as 30457 % 12500 is 5457

# 7th last digit of 2**7830457 is __0__, as 830457 % 62500 is 17957

# 8th last digit of 2**7830457 is __0__, as 7830457 % 312500 is 17957

# 9th last digit of 2**7830457 is __7__, as 7830457 % 1562500 is 17957

#10th last digit of 2**7830457 is __9__, as 7830457 % 7812500 is 17957

# In fact, (1 << 17957) % 10000000000 gives 9700303872
# Now the problem simplifies to find the last 10 digits of 28433*9700303872+1

__sum__ = 0
for ind, num in enumerate(reversed('28433')):
    num = (int(num) * 10 ** ind * 9700303872) % 10 ** 10
    __sum__ += num
    __sum__ %= 10 ** 10
__sum__ += 1

print(__sum__)
