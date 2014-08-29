class Solution:
    # @return an integer
    def uniquePaths(self, m, n): # m = n_rows, n = n_cols

        # keep one row
        current_row = [1] * n

        for ind_row in reversed(range(m - 1)):
            last_row = current_row[:]
            current_row[-1] = 1
            for ind_col in reversed(range(n - 1)):
                current_row[ind_col] = current_row[ind_col + 1] + last_row[ind_col]

        return current_row[0]
