# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        solutions = []
        current_level = [root]
        while current_level:
            solutions = [[node.val for node in current_level]] + solutions
            previous_level = current_level
            current_level = []
            for node in previous_level:
                if node.left and node.right:
                    current_level.extend([node.left, node.right])
                elif node.left:
                    current_level.extend([node.left])
                elif node.right:
                    current_level.extend([node.right])
        return solutions
