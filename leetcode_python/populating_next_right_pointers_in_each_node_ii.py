# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        current = [root]
        while len(current) > 0:
            last = current
            current = []
            for node in last:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            for ind, node in enumerate(current[:-1]):
                node.next = current[ind + 1]
        return
