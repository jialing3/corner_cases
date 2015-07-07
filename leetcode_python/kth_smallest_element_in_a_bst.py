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
        # in-order traversal
        nodes_to_visit = [] # FILO
        current = root
        cnt = 0
        while current or len(nodes_to_visit):
            if current:
                nodes_to_visit.append(current)
                current = current.left
            else:
                current = nodes_to_visit.pop() # FILO
                cnt += 1
                if cnt == k:
                    return current.val
                current = current.right
