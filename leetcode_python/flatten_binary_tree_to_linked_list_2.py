# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        current_node = None
        nodes_to_visit = [root]
        while nodes_to_visit:
            last_node = current_node
            current_node = nodes_to_visit.pop() # last element
            if last_node:
                last_node.right = current_node
                last_node.left = None
            if current_node.right:
                nodes_to_visit.append(current_node.right)
            if current_node.left:
                nodes_to_visit.append(current_node.left)
        return
