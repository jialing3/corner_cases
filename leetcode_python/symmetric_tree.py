# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        elif not left:
            return False
        elif not right:
            return False

        if left.val != right.val:
            return False
        elif not self.isMirror(left.left, right.right):
            return False
        else:
            return self.isMirror(left.right, right.left)


    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        
