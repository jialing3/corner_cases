


def get_square_length(p_0, p_1):
    return (p_0[0] - p_1[0]) ** 2 + (p_0[1] - p_1[1]) ** 2

def check_is_right_triangle(P, Q):
    O = (0, 0)
    OP = get_square_length(O, P)
    OQ = get_square_length(O, Q)
    PQ = get_square_length(P, Q)
    squared_legs = [OP, OQ, PQ]
    squared_legs.sort()
    return squared_legs[2] == squared_legs[0] + squared_legs[1]

def get_possible_points(x_list, y_list):
    possible_points = []
    for x in x_list:
        for y in y_list:
            if not (x == 0 and y == 0):
                possible_points.append((x, y))
    return possible_points

def get_num_of_possible_right_triangles(max_range_of_x_and_y):
    x_list = list(range(0, max_range_of_x_and_y))
    y_list = list(range(0, max_range_of_x_and_y))
    possible_points = get_possible_points(x_list, y_list)

    num_of_right_triangles = 0
    for ind_P, P in enumerate(possible_points):
        for ind_Q in range(ind_P + 1, len(possible_points)):
            Q = possible_points[ind_Q]
            if check_is_right_triangle(P, Q) is True:
                num_of_right_triangles += 1
                #print(P, Q)
    return num_of_right_triangles

assert(get_num_of_possible_right_triangles(3) == 14)
print(get_num_of_possible_right_triangles(51))

# There is a generation process that can be applied to simply the problem
# (0,0), (x,y) and (x-cy,cx+y) form a right triangle

# Another possible solution is to look at the slopes, or the dot product of vectors
