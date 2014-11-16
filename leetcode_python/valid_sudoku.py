# [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

class Solution:
    def is_valid_cell(self, cell): # redundant numbers
        cell.sort()
        for ind in range(len(cell) - 1):
            if cell[ind] == cell[ind + 1] and cell[ind] != '.':
                return False
        return True

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in board:
            if not self.is_valid_cell(list(row)):
                return False
        for i in range(9):
            if not self.is_valid_cell([row[i] for row in board]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.is_valid_cell([board[x][y] for x in range(3 * i, 3 * (i + 1)) for y in range(3 * j, 3 * (j + 1))]):
                    return False
        return True
