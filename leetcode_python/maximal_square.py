class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        max_area = 0
        for ind in range(len(matrix)):
            if ind == 0:
                current_row = [int(x) for x in matrix[0]]
            else:
                current_row = [0 if matrix[ind][j] == '0' else current_row[j] + 1 for j in range(len(current_row))]
            stack = [0]
            current_row = [0] + current_row + [0]
            #print current_row
            for j in range(1, len(current_row)):
                while stack and current_row[j] <= current_row[stack[-1]]: # smaller height than the top of stack
                    j_popped = stack.pop()
                    height = current_row[j_popped]
                    width = (j - stack[-1] - 1) if stack else 1 # 1
                    max_area = max(max_area, min(height, width) ** 2) # min
                stack.append(j)
            current_row = current_row[1:-1]
        return max_area
