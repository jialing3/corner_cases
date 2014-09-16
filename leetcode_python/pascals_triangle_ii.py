class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        current_row = [1]
        for ind in range(1, rowIndex + 1):
            current_row = [1] + [current_row[j] + current_row[j + 1] for j in range(ind - 1)] + [1]
        return current_row
