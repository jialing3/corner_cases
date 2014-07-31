# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        vals = []

        def inorder_traversal(node, vals):
            if node is None:
                return
            inorder_traversal(node.left, vals)
            vals.append(node.val)
            inorder_traversal(node.right, vals)
            return

        inorder_traversal(root, vals)

        for i in range(1, len(vals)):
            if vals[i - 1] >= vals[i]:
                return False
        else:
            return True
