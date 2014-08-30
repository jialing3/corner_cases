# Keep a stack, LIFO

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        tmp = []
        nodes_to_visit = [] # stack
        if root:
            nodes_to_visit.append(root)

        while nodes_to_visit:
            current_node = nodes_to_visit.pop() # last element
            tmp.append(current_node.val)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
            if current_node.left:
                nodes_to_visit.append(current_node.left) # note left in later
        return tmp
