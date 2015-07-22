class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        matrix = [[int(col) for col in row] for row in matrix]

        m = len(matrix)
        n = len(matrix[0])
        max_area = self.max_rectangle_per_row(matrix[0])
        for row in range(1, m):
            matrix[row] = [matrix[row - 1][col] + 1 if matrix[row][col] != 0 else 0 for col in range(n)]
            max_area = max(max_area, self.max_rectangle_per_row(matrix[row]))

        return max_area


    def max_rectangle_per_row(self, row):
        row_copy = [0] + row + [0]
        stack = [0] # ind
        max_area = 0
        for i, y in enumerate(row_copy):
            while stack and y <= row_copy[stack[-1]]: # row_copy
                popped_i = stack.pop()
                max_area = max(max_area, row_copy[popped_i] * (i - stack[-1] - 1 if stack else 1)) # row_copy[popped_i]
            stack.append(i) # key
        return max_area
