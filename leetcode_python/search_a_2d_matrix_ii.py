# binary search

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        #print matrix
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        elif matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        else:
            m = len(matrix)
            n = len(matrix[0])
            if m == n == 1:
                return matrix[0][0] == target
            elif n == 1:
                return self.searchMatrix([[col for row in matrix for col in row]], target)
            elif m == 1:
                # 1-d
                if matrix[0][n / 2] == target:
                    return True
                elif matrix[0][n / 2] > target:
                    return self.searchMatrix([matrix[0][:n / 2]], target)
                else:
                    return self.searchMatrix([matrix[0][n / 2:]], target)
            else:
                if matrix[m / 2][n / 2] == target:
                    return True
                elif matrix[m / 2][n / 2] > target:
                    return self.searchMatrix([[matrix[row][col] for col in range(n / 2)] for row in range(m / 2)], target) or self.searchMatrix([[matrix[row][col] for col in range(n / 2, n)] for row in range(m / 2)], target) or self.searchMatrix([[matrix[row][col] for col in range(n / 2)] for row in range(m / 2, m)], target)
                else:
                    return self.searchMatrix([[matrix[row][col] for col in range(n / 2 + 1, n)] for row in range(m / 2 + 1, m)], target) or self.searchMatrix([[matrix[row][col] for col in range(n / 2 + 1, n)] for row in range(m / 2 + 1)], target) or self.searchMatrix([[matrix[row][col] for col in range(n / 2 + 1)] for row in range(m / 2 + 1, m)], target)
