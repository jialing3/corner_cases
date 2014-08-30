# three conditions:
# 1) traversing down
# 2) traversing up from left
# 3) traversing up from right

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        tmp = []
        nodes_to_visit = [] # stack
        if root:
            nodes_to_visit.append(root)
        previous_node = None
        while nodes_to_visit:
            current_node = nodes_to_visit[-1] # not pop
            if previous_node is None or current_node in (previous_node.left, previous_node.right):
                if current_node.left:
                    nodes_to_visit.append(current_node.left)
                elif current_node.right:
                    nodes_to_visit.append(current_node.right)
                else: # leaf node
                    tmp.append(current_node.val)
                    nodes_to_visit.pop()
            elif previous_node == current_node.left:
                if current_node.right:
                    nodes_to_visit.append(current_node.right)
                else: # no right child
                    tmp.append(current_node.val)
                    nodes_to_visit.pop()
            elif previous_node == current_node.right:
                tmp.append(current_node.val)
                nodes_to_visit.pop()
            previous_node = current_node
        return tmp
