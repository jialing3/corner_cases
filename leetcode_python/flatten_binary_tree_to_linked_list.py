# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):

        if not root:
            return

        def pre_order(node, previous):
            if previous:
                previous.right = node
                previous.left = None

            # recurse
            remember_right = node.right if node.right else None
            remember_left = node.left if node.left else None
            if remember_left:
                left = pre_order(remember_left, node)
            if remember_right:
                right = pre_order(remember_right, left if remember_left else node)

            # return the previous node for the next round
            if remember_right:
                return right
            elif remember_left:
                return left
            else:
                return node

        pre_order(root, None)
        return root
