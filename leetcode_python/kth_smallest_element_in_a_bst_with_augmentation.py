# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        self.update_tree(root)
        while root:
            left_size = 0 if not root.left else root.left.size
            if left_size + 1 == k:
                return root.val
            elif k > left_size:
                k = k - 1 - left_size
                root = root.right
            else:
                root = root.left


    def update_tree(self, root):
        # recursive post-order traversal
        left_size = self.update_tree(root.left) if root.left else 0
        right_size = self.update_tree(root.right) if root.right else 0
        root.size = left_size + right_size + 1
        return root.size
