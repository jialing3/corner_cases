# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def walk(self, path, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            path.append(node.val)
            n = len(path)
            return sum(int(val) * 10 ** (n - 1 - ind) for ind, val in enumerate(path))
        left_total = 0 if node.left is None else self.walk(path + [node.val], node.left)
        right_total = 0 if node.right is None else self.walk(path + [node.val], node.right)
        return left_total + right_total
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.walk([], root)
