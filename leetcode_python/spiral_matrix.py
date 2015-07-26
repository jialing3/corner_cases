class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        output = []
        current_i = 0
        current_j = 0

        while m > 0 and n > 0:
            self.spiral(matrix, m, n, current_i, current_j, output)
            m -= 2
            n -= 2
            current_i += 1
            current_j += 1

        return output



    def spiral(self, matrix, m, n, current_i, current_j, output):
        if m == 1:
            # a row
            for j in range(current_j, current_j + n):
                output.append(matrix[current_i][j])
            return
        elif n == 1:
            # a column
            for i in range(current_i, current_i + m):
                output.append(matrix[i][current_j])
            return
        else:
            # spiral around: top row, right column, bottom row, left column
            for j in range(current_j, current_j + n - 1):
                output.append(matrix[current_i][j])
            for i in range(current_i, current_i + m - 1):
                output.append(matrix[i][current_j + n - 1])
            for j in reversed(range(current_j + 1, current_j + n)): # shifted by 1 to the right
                output.append(matrix[current_i + m - 1][j])
            for i in reversed(range(current_i + 1, current_i + m)): # shifted down by 1
                output.append(matrix[i][current_j])
            return
