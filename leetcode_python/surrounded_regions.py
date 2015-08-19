# find islands
# for each island, check if touching any edge

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        adjacency_list = {}
        board = list(map(list, board))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    adjacency_list[(i, j)] = []
                    for row, col in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= row < m and 0 <= col < n:
                            if board[row][col] == 'O':
                                adjacency_list[(i, j)].append((row, col))

        for node in adjacency_list.keys():
            nodes_in_neighborhood = self.find_neighborhood(node, adjacency_list)
            if all([0 < row < m - 1 and 0 < col < n - 1 for row, col in nodes_in_neighborhood]): # not touching edges
                for row, col in nodes_in_neighborhood:
                    board[row][col] = 'X'

        return

    def find_neighborhood(self, node, adjacency_list):
        nodes_to_visit = [node]
        visited = set()
        while nodes_to_visit:
            current = nodes_to_visit.pop()
            visited.add(current)
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    nodes_to_visit.append(neighbor)
        return visited
