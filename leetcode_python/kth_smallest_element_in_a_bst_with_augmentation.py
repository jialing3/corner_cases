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
            if root.left:
                if root.left.size == k - 1:
                    return root.val
                elif root.left.size >= k:
                    root = root.left
                else:
                    k = k - 1 - root.left.size
                    root = root.right
            elif k == 1:
                return root.val
            elif root.right:
                k = k - 1
                root = root.right


    def update_tree(self, root):
        # recursive post-order traversal
        left_size = self.update_tree(root.left) if root.left else 0
        right_size = self.update_tree(root.right) if root.right else 0
        root.size = left_size + right_size + 1
        return root.size
