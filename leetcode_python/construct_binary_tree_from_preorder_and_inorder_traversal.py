# root node
# assume all node values are distinct

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        len_preorder = len(preorder)
        if len_preorder == 0:
            return None
        elif len_preorder == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            root_ind = inorder.index(preorder[0])
            left_inorder, right_inorder = inorder[:root_ind], inorder[root_ind + 1:]
            left_preorder, right_preorder = preorder[1:root_ind + 1], preorder[root_ind + 1:]
            root.left = self.buildTree(left_preorder, left_inorder)
            root.right = self.buildTree(right_preorder, right_inorder)
            return root
