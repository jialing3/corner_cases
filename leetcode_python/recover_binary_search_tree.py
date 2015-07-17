# Inorder traversal should be in order. No pun intended.
# Watch out for infinite loops.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        nodes_to_visit = []
        current = root
        previous = None
        nodes_out_of_place = []

        while current or nodes_to_visit:
            if current:
                nodes_to_visit.append(current)
                current = current.left
            else:
                current = nodes_to_visit.pop() # current node is always processed before the right daughter
                if previous and previous.val > current.val:
                    nodes_out_of_place.extend([previous, current])
                previous = current
                current = current.right # but right daughters of the left branch is processed before the ancestor node
                # empty daughters signify "done" with a branch and jump to the else condition, avoiding infinite loops

        self.swap_last_and_first_vals(nodes_out_of_place)
        return

    def swap_last_and_first_vals(self, nodes):
        nodes[0].val, nodes[-1].val = nodes[-1].val, nodes[0].val
