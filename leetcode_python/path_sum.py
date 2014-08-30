# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        tmp = [] # store sums from leaf nodes
        current_level = [root]
        current_level_sum = [root.val]
        while current_level:
            previous_level = current_level
            previous_level_sum = current_level_sum
            current_level = []
            current_level_sum = []
            for node, node_sum in zip(previous_level, previous_level_sum):
                if node.left:
                    current_level.append(node.left)
                    current_level_sum.append(node_sum + node.left.val)
                if node.right:
                    current_level.append(node.right)
                    current_level_sum.append(node_sum + node.right.val)
                if node.left is None and node.right is None: # leaf node
                    tmp.append(node_sum)
        return sum in tmp
