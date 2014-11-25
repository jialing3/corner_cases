# BFS
# example ["aaaa","aaaa","aaaa","aaaa","aaab"], "aaaaaaaaaaaaaaaaaaaa"
# Berkeley AI course covers Search
#
# BFS explodes for longer words, if we keep full track of path history
#
# save on representation of the path, by only keeping the last position and the area covered (can afford to lose the sequence prior to the last position)

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist_base(self, board, word):
        num_rows = len(board)
        num_cols = len(board[0])
        current_letter_positions = set(((i, j), ()) for i in range(num_rows) for j in range(num_cols) if board[i][j] == word[0])
        # keep the last node, and the set of previous nodes visited
        for letter in word[1:]:
            if not current_letter_positions:
                return [] # False
            next_letter_positions = set()
            current_letters = dict((x[0], None) for x in current_letter_positions)
            for i, j in current_letters.iterkeys():
                tmp_next = [(i + m, j + n) for m, n in ((-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= i + m < num_rows and 0 <= j + n < num_cols and board[i + m][j + n] == letter] # list of potential next position, not considering area covered by previous positions
                current_letters[(i, j)] = tmp_next
            #print current_letters
            for current_track in current_letter_positions:
                i, j = current_track[0]
                track_set = set(current_track[1])
                tmp_next = [pos for pos in current_letters[(i, j)] if pos not in track_set] # check not seen previously
                track_set.add((i, j))
                tmp_next = [(pos, tuple(sorted(track_set))) for pos in tmp_next]
                next_letter_positions.update(tmp_next)
            current_letter_positions = next_letter_positions
            #print len(current_letter_positions), len(current_letters)
        return current_letter_positions # len(current_letter_positions) > 0

    def exist(self, board, word):
        return len(self.exist_base(board, word)) > 0
