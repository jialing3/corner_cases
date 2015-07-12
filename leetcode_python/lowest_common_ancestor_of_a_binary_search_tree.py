# start from root, see when divergence happens

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current and current.left and current.right:
            if current.val < min(p.val, q.val): # current node too small, traverse right
                current = current.right
            elif current.val > max(p.val, q.val): # current node too large, traverse left
                current = current.left
            else:
                break
        return current
