# Each cell has three constraints: 1) row, 2) column and 3) little square

# constraint propagation
# (1) If a square has only one possible value, then eliminate that value from the square's peers.
# (2) If a unit has only one possible place for a value, then put the value there.

# DFS, try a possible value and see if this leads to any contradiction, make a copy of board each time

# Because changes need to be made in-place, keep track of changes!
# http://norvig.com/sudoku.html

'''
board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
'''

class Solution:
    def get_row(self, row_num, board):
        return set(x for x in board[row_num] if x != '.')


    def get_col(self, col_num, board):
        return set(row[col_num] for row in board if row[col_num] != '.')


    def get_sq(self, row_num, col_num, board):
        row_num = row_num / 3 * 3
        col_num = col_num / 3 * 3
        return set(board[i][j] for i in range(row_num, row_num + 3) for j in range(col_num, col_num + 3) if board[i][j] != '.')


    def get_peers(self, row, col, board):
        row_num, col_num = row / 3 * 3, col / 3 * 3
        peer_list = [[row, j] for j in range(len(board[0])) if j != col and board[row][j] == '.'] + [[i, col] for i in range(len(board)) if i != row and board[i][col] == '.'] + [[i, j] for i in range(row_num, row_num + 3) for j in range(col_num, col_num + 3) if board[i][j] == '.' and not (i == row and j == col)]
        return peer_list


    def get_units(self, row, col, board):
        row_num, col_num = row / 3 * 3, col / 3 * 3
        unit_lists = [[]] * 3
        unit_lists[0] = [[row, j] for j in range(len(board[0])) if j != col]
        unit_lists[1] = [[i, col] for i in range(len(board)) if i != row]
        unit_lists[2] = [[i, j] for i in range(row_num, row_num + 3) for j in range(col_num, col_num + 3) if not (i == row and j == col)]
        return unit_lists


    def get_unused_elements(self, row, col, board):
        if board[row][col] == '.':
            return set(str(n) for n in range(1, 10)) - (self.get_row(row, board) | self.get_col(col, board) | self.get_sq(row, col, board))
        else:
            return set([board[row][col]])


    def count_empty_slots(self, board):
        return len([x for row in board for x in row if x == '.'])


    def sweep(self, board):
        changes = []
        starting_number_of_empty_slots = self.count_empty_slots(board)
        possible_values = [[self.get_unused_elements(i, j, board) for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # strategy # 1
                if len(possible_values[i][j]) == 1:
                    value = list(possible_values[i][j])[0]
                    board[i][j] = value
                    changes.append([i, j, value])
                    if not self.isvalid(board):
                        board[i][j] = '.'
                        return 1, [] # positive_number
                    peers = self.get_peers(i, j, board)
                    for k, l in peers:
                        if value in possible_values[k][l]:
                            possible_values[k][l].remove(value)
                            if len(possible_values[k][l]) == 1:
                                board[k][l] = list(possible_values[k][l])[0]
                # strategy # 2
                else:
                    units = self.get_units(i, j, board)
                    for value in possible_values[i][j]:
                        if any(all(value not in possible_values[k][l] for k, l in unit) for unit in units):
                            possible_values[i][j] = set([value])
                            board[i][j] = value
                            changes.append([i, j, value])
                            if not self.isvalid(board):
                                board[i][j] = '.'
                                return 1, [] # positive_number
                            break
        return self.count_empty_slots(board) - starting_number_of_empty_slots, changes


    def contains_duplicates(self, non_empty_entries):
        return len(non_empty_entries) != len(set(non_empty_entries))


    def isvalid(self, board):
        for row_num in range(len(board)):
            row = [x for x in board[row_num] if x != '.']
            if self.contains_duplicates(row):
                return False
        for col_num in range(len(board[0])):
            col = [row[col_num] for row in board if row[col_num] != '.']
            if self.contains_duplicates(col):
                return False
        for row_num in range(0, len(board), 3):
            for col_num in range(0, len(board[0]), 3):
                row_num = row_num / 3 * 3
                col_num = col_num / 3 * 3
                sq = [board[i][j] for i in range(row_num, row_num + 3) for j in range(col_num, col_num + 3) if board[i][j] != '.']
                if self.contains_duplicates(sq):
                    return False
        return True


    def get_branches(self, board):
        possible_values = [[self.get_unused_elements(i, j, board) for j in range(len(board[0]))] for i in range(len(board))]
        len_possibilities = [[i, j, len(possible_values[i][j])] for i in range(len(board)) for j in range(len(board[0])) if len(possible_values[i][j]) > 1]
        len_possibilities.sort(key=lambda x: x[2])
        return [(i, j, possible_values[i][j]) for i, j, _ in len_possibilities]


    def walk(self, board):
        if self.count_empty_slots(board) == 0:
            return True
        branches = self.get_branches(board)
        for i, j, value_set in branches:
            for value in sorted(value_set):
                board[i][j] = value
                delta, changes = self.sweep(board)
                if not self.isvalid(board):
                    board[i][j] = '.'
                    for k, l, u in changes:
                        board[k][l] = '.'
                else:
                    tmp = self.walk(board)
                    if tmp:
                        return tmp
                    else:
                        board[i][j] = '.'
                        for k, l, u in changes:
                            board[k][l] = '.'
        return False



    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        delta = -1
        while delta < 0:
            delta, _ = self.sweep(board)
        self.walk(board)
        return
