# dynamic programming

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        running_counts = [None] * n
        running_counts[0] = 0 if obstacleGrid[0][0] == 1 else 1
        for j in range(1, n):
            running_counts[j] = 0 if obstacleGrid[0][j] == 1 or running_counts[j - 1] == 0 else 1
        for i in range(1, m):
            running_counts[0] = 0 if obstacleGrid[i][0] == 1 or running_counts[0] == 0 else 1
            for j in range(1, n):
                running_counts[j] = 0 if obstacleGrid[i][j] == 1 else running_counts[j - 1] + running_counts[j]
        return running_counts[-1]
