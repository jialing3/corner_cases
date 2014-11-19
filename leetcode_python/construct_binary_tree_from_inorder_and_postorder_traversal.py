# postorder gives away root!
# assume the nodes don't repeat

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        len_postorder = len(postorder)
        if len_postorder == 0:
            return None
        elif len_postorder == 1:
            return TreeNode(postorder[-1])
        else:
            root = TreeNode(postorder[-1])
            root_ind = inorder.index(postorder[-1])
            left_inorder, right_inorder = inorder[:root_ind], inorder[root_ind + 1:]
            left_postorder, right_postorder = postorder[:root_ind], postorder[root_ind:-1]
            # sorted(left_inorder) == sorted(left_postorder)
            # sorted(right_inorder) == sorted(right_postorder)
            left = self.buildTree(left_inorder, left_postorder)
            right = self.buildTree(right_inorder, right_postorder)
            root.left = left
            root.right = right
            return root
            
