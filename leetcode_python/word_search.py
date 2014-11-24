# BFS
# example ["aaaa","aaaa","aaaa","aaaa","aaab"], "aaaaaaaaaaaaaaaaaaaa"

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])
        current_letter_positions = [[(i, j)] for i in range(num_rows) for j in range(num_cols) if board[i][j] == word[0]]
        # keep a trace
        for letter in word[1:]:
            if not current_letter_positions:
                return False
            next_letter_positions = []
            for current_track in current_letter_positions:
                i, j = current_track[-1]
                tmp_next = [(i + m, j + n) for m in (-1, 1) for n in (-1, 1) if 0 <= i + m < num_rows and 0 <= j + n < num_cols and (i + m, j + n) not in current_track[:-1] and board[i + m][j + n] == letter] # check not seen
                tmp_next = [current_track + [(i_new, j_new)] for i_new, j_new in tmp_next]
                next_letter_positions.extend(tmp_next)
            current_letter_positions = next_letter_positions
        return len(current_letter_positions) > 0
