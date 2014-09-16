class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        current_row = [1]
        solution = [current_row]
        for ind in range(1, numRows):
            current_row = [1] + [current_row[j] + current_row[j + 1] for j in range(ind - 1)] + [1]
            solution.append(current_row)
        return solution
