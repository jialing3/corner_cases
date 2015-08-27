class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        words_trie = {}
        for w in words:
            tmp = words_trie
            for ind, letter in enumerate(w):
                if letter not in tmp:
                    tmp[letter] = {}
                if ind < len(w) - 1:
                    tmp = tmp[letter]
                else: # ind < len(w) - 1
                    tmp[letter]['__end__'] = w


        m, n = len(board), len(board[0])
        output = set()
        for i in range(m):
            for j in range(n):
                for w in self.find_words_starting_from_cell((i, j), board, words_trie):
                    output.add(w)
        return list(output)

    def find_words_starting_from_cell(self, cell, board, words_trie):
        m, n = len(board), len(board[0])
        row, col = cell
        current_level = [(cell, words_trie[board[row][col]], set())] if board[row][col] in words_trie else []
        output = set()
        while current_level:
            next_level = []
            for node in current_level:
                (row, col), tmp, visited_set = node
                if '__end__' in tmp:
                    output.add(tmp['__end__'])
                for i, j in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in visited_set and board[i][j] in tmp:
                        next_level.append(((i, j), tmp[board[i][j]], visited_set | set([(row, col)])))
            current_level = next_level[:]
        return output
