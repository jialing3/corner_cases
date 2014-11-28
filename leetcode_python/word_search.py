# DFS
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        board = [list(x) for x in board]
        self.num_rows = len(board)
        self.num_cols = len(board[0])
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if board[i][j] == word[0]:
                    cnt = 1
                    board[i][j] = '.' # mark position taken
                    if self.exist_recurse(board, word[1:], i, j):
                        return True
                    else:
                        board[i][j] = word[0]

        return False

    def exist_recurse(self, board, word, i, j):
        #print board
        if not word:
            return True
        for m, n in ((-1, 0), (1, 0), (0, -1), (0, 1)): # left, right, down, up
            if 0 <= i + m < self.num_rows and 0 <= j + n < self.num_cols and board[i + m][j + n] == word[0]:
                board[i + m][j + n] = '.'
                if self.exist_recurse(board, word[1:], i + m, j + n):
                    return True
                else:
                    board[i + m][j + n] = word[0]
        return False

                                
