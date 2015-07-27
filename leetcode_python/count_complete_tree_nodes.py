# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes at the last level h.
# need to figure out how many of the last-level nodes are filled.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        node = root
        h_left, h_right = 0, 0
        while node:
            h_left += 1
            node = node.left
        node = root
        while node:
            h_right += 1
            node = node.right
        if h_left == h_right:
            return 2 ** h_left - 1
        else:
            return self.countNodes(root.left) + 1 + self.countNodes(root.right)
            
