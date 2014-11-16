class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        current = triangle[0]
        for i in range(1, len(triangle)):
            current = [current[0]] + current + [current[-1]] # pad two ends
            current = [element + min(current[i], current[i + 1]) for i, element in enumerate(triangle[i])]
        return min(current)
