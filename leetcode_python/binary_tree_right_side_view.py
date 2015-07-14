# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        current_level = []
        if root:
            current_level.append(root)

        output = []
        while current_level:
            next_level = []
            for node in current_level:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            output.append(current_level[0].val)
            current_level = next_level

        return output
