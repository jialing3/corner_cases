# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        left_nodes_to_visit = []
        right_nodes_to_visit = []
        if root:
            left_nodes_to_visit.append(root)
            right_nodes_to_visit.append(root)

        while left_nodes_to_visit and right_nodes_to_visit:
            left_current = left_nodes_to_visit.pop()
            right_current = right_nodes_to_visit.pop()

            # in-order traversal
            if left_current.val != right_current.val:
                return False

            if left_current.right and right_current.left:
                left_nodes_to_visit.append(left_current.right)
                right_nodes_to_visit.append(right_current.left)
            elif bool(left_current.right) ^ bool(right_current.left):
                return False
            #else: # both null
            #    pass

            if left_current.left and right_current.right:
                left_nodes_to_visit.append(left_current.left)
                right_nodes_to_visit.append(right_current.right)
            elif bool(left_current.left) ^ bool(right_current.right):
                return False
            #else: # both null
            #    pass

        return True
            
