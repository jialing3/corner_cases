# BFS
# example ["aaaa","aaaa","aaaa","aaaa","aaab"], "aaaaaaaaaaaaaaaaaaaa"
# Berkeley AI course covers Search
#
# BFS explodes for longer words
# What about recursively break word into two halves? Can save work on recurring subsequences

class Solution:
    def __init__(self):
        self.memo = {}

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist_base(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])
        current_letter_positions = [[(i, j)] for i in range(num_rows) for j in range(num_cols) if board[i][j] == word[0]]
        # keep a trace
        for letter in word[1:]:
            if not current_letter_positions:
                return [] # False
            next_letter_positions = []
            for current_track in current_letter_positions:
                i, j = current_track[-1]
                tmp_next = [(i + m, j + n) for m, n in ((-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= i + m < num_rows and 0 <= j + n < num_cols and (i + m, j + n) not in current_track[:-1] and board[i + m][j + n] == letter] # check not seen
                tmp_next = [current_track + [(i_new, j_new)] for i_new, j_new in tmp_next]
                next_letter_positions.extend(tmp_next)
            current_letter_positions = next_letter_positions
        return current_letter_positions # len(current_letter_positions) > 0

    def exist_recurse(self, board, word):
        if word in self.memo:
            return self.memo[word]
        num_rows = len(board)
        num_cols = len(board[0])
        num_words = len(word)
        if num_words > 20: # and num_words * 1. / (num_rows * num_cols) > .8
            first_half_positions = self.exist_recurse(board, word[:num_words / 2 + 1])
            second_half_positions = self.exist_recurse(board, word[num_words / 2:])
            current_letter_positions = [first + second[0:] for first in first_half_positions for second in second_half_positions if first[-1] == second[0] and set(first[:-1]) & set(second[0:]) == set()]
            # check if the two halves can connect and if they don't overlap
        else:
            current_letter_positions = self.exist_base(board, word)
        self.memo[word] = current_letter_positions # memo
        return current_letter_positions

    def exist(self, board, word):
        return len(self.exist_recurse(board, word)) > 0
