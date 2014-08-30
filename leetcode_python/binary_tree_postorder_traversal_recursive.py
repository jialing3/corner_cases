# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        def postorder_traversal(node):
            if not node:
                return []
            tmp = []
            if node.left:
                tmp.extend(postorder_traversal(node.left))
            if node.right:
                tmp.extend(postorder_traversal(node.right))
            tmp.append(node.val)
            return tmp
        return postorder_traversal(root)
