class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0] * n for i in range(n)]
        def next_spot(direction, i, j):
            if direction == 'right':
                return (i, j + 1)
            elif direction == 'down':
                return (i + 1, j)
            elif direction == 'left':
                return (i, j - 1)
            else: # 'up'
                return (i - 1, j)
        def is_next_spot_available(direction, i, j):
            if direction == 'right':
                return (j + 1 < n and matrix[i][j + 1] == 0)
            elif direction == 'down':
                return (i + 1 < n and matrix[i + 1][j] == 0)
            elif direction == 'left':
                return (j - 1 >= 0 and matrix[i][j - 1] == 0)
            else: # 'up'
                return (i - 1 >= 0 and matrix[i - 1][j] == 0)
        def turn(direction):
            if direction == 'right':
                return 'down'
            elif direction == 'down':
                return 'left'
            elif direction == 'left':
                return 'up'
            else: # 'up'
                return 'right'
        direction = 'right'
        i = 0
        j = 0
        for number in range(1, n ** 2 + 1):
            matrix[i][j] = number
            if is_next_spot_available(direction, i, j) is False:
                direction = turn(direction)
            i, j = next_spot(direction, i, j)
        return matrix
