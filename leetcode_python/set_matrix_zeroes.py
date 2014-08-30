# first find a zero element i, j
# store i, j externally
# use the i-th row and the j-th column to mark which additional rows and columns needed to be set to zero
# at last, restore the i-th row and the j-th column to zero

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        def find_first_zero(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        return i, j # python doesn't break out of double for loops
            else:
                return -1, -1
        i_row, j_col = find_first_zero(matrix)
        if i_row == -1:
            return
        # can leave all the zeros in the i-th row and the j-th column intact
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and i != i_row and j != j_col:
                    matrix[i][j_col] = 0
                    matrix[i_row][j] = 0
        # actual flipping now
        for j in range(len(matrix[0])):
            if matrix[i_row][j] == 0:
                for i in range(len(matrix)):
                    if i != i_row and j != j_col:
                        matrix[i][j] = 0
        for i in range(len(matrix)):
            if matrix[i][j_col] == 0:
                for j in range(len(matrix[0])):
                    if j != j_col and i != i_row:
                        matrix[i][j] = 0
        for j in range(len(matrix[0])):
            matrix[i_row][j] = 0
        for i in range(len(matrix)):
            matrix[i][j_col] = 0
