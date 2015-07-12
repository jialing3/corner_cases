# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        nodes_to_visit = []
        if root:
            nodes_to_visit.append(root)
        while nodes_to_visit:
            current = nodes_to_visit.pop()
            if current.right:
                nodes_to_visit.append(current.right)
            if current.left:
                nodes_to_visit.append(current.left)
            current.left, current.right = current.right, current.left
        return root
