# time limit exceeded

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        count = 0
        nodes_to_visit = []
        current = root
        while current or nodes_to_visit:
            if current:
                nodes_to_visit.append(current)
                current = current.left
            else:
                current = nodes_to_visit.pop()
                count += 1
                current = current.right
        return count
