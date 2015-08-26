class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        words_map = {} # eg. for 'eat', {'e': Fasle, 'ea': False, 'eat': True}
        for w in words:
            for i in range(1, len(w)):
                if w[:i] not in words_map:
                    words_map[w[:i]] = False
            words_map[w] = True

        m, n = len(board), len(board[0])
        output = []
        for i in range(m):
            for j in range(n):
                output.extend(self.find_words_starting_from_cell((i, j), board, words_map))
        return output

    def find_words_starting_from_cell(self, cell, board, words_map):
        m, n =len(board), len(board[0])
        row, col = cell
        nodes_to_visit = [(cell, board[row][col])] if board[row][col] in words_map else [] # cell position and prefix
        output = []
        while nodes_to_visit:
            # DFS
            current = nodes_to_visit.pop()
            (row, col), prefix = current
            for i, j in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if 0 <= i < m and 0 <= j < n and prefix + board[i][j] in words_map:
                    nodes_to_visit.append(((i, j), prefix + board[i][j]))
                    if words_map[prefix + board[i][j]] is True:
                        output.append(prefix + board[i][j])
        return output
