# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        current = set([root])
        level = 0
        while len(current) > 0:
            level += 1
            last = current
            current = set()
            for node in last:
                if node.left:
                    current.add(node.left)
                if node.right:
                    current.add(node.right)
        return level
        
