# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        tmp = []
        nodes_to_visit = [] # stack
        current_node = root
        while current_node or len(nodes_to_visit) > 0:
            if current_node:
                nodes_to_visit.append(current_node)
                current_node = current_node.left
            else:
                current_node = nodes_to_visit.pop()
                tmp.append(current_node.val)
                current_node = current_node.right
        return tmp
