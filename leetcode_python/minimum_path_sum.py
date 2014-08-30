class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        def cumsum(it):
            total = 0
            for x in it:
                total += x
                yield total

        current_row = list(cumsum(reversed(grid[-1])))
        current_row.reverse()

        for i in reversed(range(len(grid) - 1)):
            last_row = current_row
            current_row[-1] = last_row[-1] + grid[i][-1]
            for j in reversed(range(len(grid[0]) - 1)):
                current_row[j] = min(current_row[j + 1], last_row[j]) + grid[i][j]

        return current_row[0]
