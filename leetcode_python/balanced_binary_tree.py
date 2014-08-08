# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def getHeight(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1

        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        if left == -1 or right == -1:
            return -1
        elif abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1

    def isBalanced(self, root):
        return not(self.getHeight(root) == -1)
