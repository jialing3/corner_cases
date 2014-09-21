# BFS

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        current = [root]
        level = 1
        while current:
            past = current
            current = []
            for node in past:
                if not node.left and not node.right:
                    return level
                else:
                    if node.left:
                        current.append(node.left)
                    if node.right:
                        current.append(node.right)
            level += 1
                    
