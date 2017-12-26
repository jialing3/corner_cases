from itertools import combinations

lst_of_squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

cube_0 = set(['0', '5', '6', '7', '8', '9'])
cube_1 = set(['1', '2', '3', '4', '8', '9'])

def flip_6_or_9(cube):
    if '6' in cube:
        cube.add('9')
    if '9' in cube:
        cube.add('6')
    return

def check_if_all_squares_are_covered(cube_0, cube_1, lst_of_squares):
    # Ideally, should have kept cube_0 and cube_1 intact
    flip_6_or_9(cube_0)
    flip_6_or_9(cube_1)

    # bottom-up
    all_numbers_formed = set()
    for digit_0 in cube_0:
        for digit_1 in cube_1:
            all_numbers_formed.add(digit_0 + digit_1)
            all_numbers_formed.add(digit_1 + digit_0)
    for square_num in lst_of_squares:
        if square_num not in all_numbers_formed:
            return False
    return True

def get_all_cubes():
    return list(map(set, combinations('0123456789', 6)))

all_cubes = get_all_cubes()
count_of_working_set_of_two_cubes = 0
for ind_0, cube_0 in enumerate(all_cubes):
    for ind_1 in range(ind_0, len(all_cubes)):
        cube_1 = all_cubes[ind_1]
        if check_if_all_squares_are_covered(cube_0, cube_1, lst_of_squares):
            count_of_working_set_of_two_cubes += 1

print(count_of_working_set_of_two_cubes)
