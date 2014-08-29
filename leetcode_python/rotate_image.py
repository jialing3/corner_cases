class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):

        n_rows = n_cols = len(matrix)

        # flip around the diagonal
        for i in range(n_rows):
            for j in range(i + 1, n_cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip left and right for each row
        for ind, row in enumerate(matrix):
            matrix[ind] = row[::-1]

        return matrix
