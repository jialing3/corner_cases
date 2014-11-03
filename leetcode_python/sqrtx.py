class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return x
        root = 1
        while not root ** 2 <= x < (root + 1) ** 2:
            root = (root + x / root) / 2
        return root
        
