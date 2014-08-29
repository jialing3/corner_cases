
# breadth first search

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        x_s = range(n) # initialize x positions


        def find_y_for_next_queen(previous, level):
            current = []
            for i in range(n):
                if i not in previous and not any(abs(x_s[p] - x_s[level]) == abs(previous[p] - i) for p in range(level)):
                    current.append(previous + [i])
            return current


        previous_lst = [[]]
        for level in range(n):
            current_lst = []
            for previous in previous_lst:
                current_lst.extend(find_y_for_next_queen(previous, level))
            previous_lst = current_lst


        solutions = []
        for y_s in current_lst:
            layouts = [['.'] * n for i in range(n)] # not referenced to the same '.'
            for x, y in zip(x_s, y_s):
                layouts[x][y] = 'Q'
            solutions.append([''.join(row) for row in layouts])
        return len(solutions)
