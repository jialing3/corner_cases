# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None

        n = len(num) / 2
        node = TreeNode(num[n])
        node.left = self.sortedArrayToBST(num[:n])
        node.right = self.sortedArrayToBST(num[n + 1:])
        return node
        
