'''
let x be the length_of_two_sides
then height = sqrt( (1.5 x +/- 0.5) (0.5x -/+ 0.5) )
if x is even, then height needs to be even
if x is odd, then height needs to be int

for y in range(1, 10 ** 9 // 4 + 1)
x = 2y covers the even cases
x = 2y + 1 covers the odd cases

but, the *real* problem here is there exists
a precision issue for large y

when y = 46302366, if we take the case of x = 2y + 1,
and look for ( (3 * y + 2) * y ) ** 0.5,
we'll get 80198051,
whose square is 6431727384198601, not 6431727384198600

(tmp ** 0.5) ** 2 == tmp takes care of the precision issue
'''


total_perimeter = 0
for y in range(1, 10 ** 9 // 6 + 1):
    # x = 2y, need sqrt( (3y +/- 0.5) (y -/+ 0.5) ) to be even
    tmp_0 = 3 * y + 0.5
    tmp_1 = y - 0.5
    if tmp_0 % 2 == 0 or tmp_1 % 2 == 0:
        tmp = tmp_0 * tmp_1
        if tmp % 4 == 0:
            if (tmp ** 0.5) % 1 == 0 and int(tmp ** 0.5) ** 2 == tmp:
                perimeter = 6 * y + 1
                total_perimeter += perimeter
                print(2 * y, 2 * y, 2 * y + 1, perimeter)
    tmp_0 = 3 * y - 0.5
    tmp_1 = y + 0.5
    if tmp_0 % 2 == 0 or tmp_1 % 2 == 0:
        tmp = tmp_0 * tmp_1
        if tmp % 4 == 0:
            if (tmp ** 0.5) % 1 == 0 and int(tmp ** 0.5) ** 2 == tmp:
                perimeter = 6 * y - 1
                total_perimeter += perimeter
                print(2 * y, 2 * y, 2 * y - 1, perimeter)
    # x = 2y + 1, need sqrt( (3y + 1.5 +/- 0.5) (y + 0.5 -/+ 0.5) ) to be int
    tmp = (3 * y + 2) * y
    if (tmp ** 0.5) % 1 == 0 and int(tmp ** 0.5) ** 2 == tmp:
        perimeter = 6 * y + 4
        total_perimeter += perimeter
        print(2 * y + 1, 2 * y + 1, 2 * y + 2, perimeter)
    tmp = (3 * y + 1) * (y + 1)
    if (tmp ** 0.5) % 1 == 0 and int(tmp ** 0.5) ** 2 == tmp:
        perimeter = 6 * y + 2
        total_perimeter += perimeter
        print(2 * y + 1, 2 * y + 1, 2 * y, perimeter)

print(total_perimeter)

# Alternatively, one could resort to using pythagorean triples
