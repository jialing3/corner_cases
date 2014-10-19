# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, _sum_):
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == _sum_:
                return [[root.val]]
            else:
                return []
        elif root.left and root.right:
            remaining = self.pathSum(root.left, _sum_ - root.val)
            remaining.extend(self.pathSum(root.right, _sum_ - root.val))
        elif root.left:
            remaining = self.pathSum(root.left, _sum_ - root.val)
        else:
            remaining = self.pathSum(root.right, _sum_ - root.val)
        return [[root.val] + remaining_path for remaining_path in remaining]
