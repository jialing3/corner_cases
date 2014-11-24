# BFS

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])
        current_letter_positions = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == word[0]]
        for letter in word[1:]:
            if not current_letter_positions:
                return False
            next_letter_positions = []
            for i, j in current_letter_positions:
                next_letter_positions.extend([(i + m, j + n) for m in (-1, 1) for n in (-1, 1) if 0 <= i + m < num_rows and 0 <= j + n < num_cols and board[i + m][j + n] == letter])
            current_letter_positions = next_letter_positions
        return len(current_letter_positions) > 0
