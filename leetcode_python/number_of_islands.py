class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        grid = [list(_) for _ in grid]

        m = len(grid)
        n = len(grid[0]) if grid else 0

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, m, n, grid)
                    cnt += 1

        return cnt


    def get_neighbors(self, i, j, m, n, grid):
        y_lower = max(0, i - 1)
        y_upper = min(m - 1, i + 1)
        x_lower = max(0, j - 1)
        x_upper = min(n - 1, j + 1)
        #return [(y, x) for y in range(y_lower, y_upper + 1) for x in range(x_lower, x_upper + 1) if (y, x) != (i, j) and grid[y][x] == '1']
        neighbors = []
        if y_lower != i and grid[y_lower][j] == '1':
            neighbors.append((y_lower, j))
        if y_upper != i and grid[y_upper][j] == '1':
            neighbors.append((y_upper, j))
        if x_lower != j and grid[i][x_lower] == '1':
            neighbors.append((i, x_lower))
        if x_upper != j and grid[i][x_upper] == '1':
            neighbors.append((i, x_upper))
        return neighbors


    def dfs(self, i, j, m, n, grid):
        stack = [(i, j)]
        visited = set()
        while stack:
            current_i, current_j = stack.pop()
            visited.add((current_i, current_j))
            for neighbor in self.get_neighbors(current_i, current_j, m, n, grid):
                if neighbor not in visited:
                    stack.append(neighbor)
            grid[current_i][current_j] = 0 # set to 0
        #print visited
        return
