# mark all islands that are not fully surrounded by land as '_'
# fill the rest of the islands
# change '_' back to 'O'

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        seeds_on_edge = [(0, j) for j in range(n)] + [(m - 1, j) for j in range(n)] + [(i, 0) for i in range(m)] + [(i, n - 1) for i in range(m)]
        for seed_row, seed_col in seeds_on_edge:
            if board[seed_row][seed_col] == 'O':
                nodes_to_visit = [(seed_row, seed_col)]
                while nodes_to_visit:
                    i, j = nodes_to_visit.pop()
                    board[i][j] = '_'
                    for row, col in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                        if 0 <= row <= m - 1 and 0 <= col <= n - 1:
                            if board[row][col] == 'O':
                                nodes_to_visit.append((row, col))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '_':
                    board[i][j] = 'O'

        return
