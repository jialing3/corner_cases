class Solution:
    # @return an integer
    def numTrees(self, n):
        return 1 if n <= 1 else sum(self.numTrees(i) * self.numTrees(n - 1 - i) for i in range(0, n))

# iterate through all possible root nodes, split into left and right subtrees.
