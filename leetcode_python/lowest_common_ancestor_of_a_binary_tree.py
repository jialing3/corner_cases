# harder than lowest common ancestor for a BST
# quote from Stephen: search for both targets together


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        return self.find_node(root, p, q)[2]


    def find_node(self, node, target1, target2):
        # return if target1 is found, if target2 is found, the least common ancestor

        # current node
        target1_found = node == target1
        target2_found = node == target2
        # previous nodes
        target1_found_left, target2_found_left, lca_left = self.find_node(node.left, target1, target2) if node.left else (False, False, None)
        target1_found_right, target2_found_right, lca_right = self.find_node(node.right, target1, target2) if node.right else (False, False, None)

        # previously found
        if lca_left:
            return True, True, lca_left
        elif lca_right:
            return True, True, lca_right
        # convergent on current level
        elif any([target1_found_left, target1_found_right, target1_found]) and any([target2_found_left, target2_found_right, target2_found]):
            return True, True, node
        # non-convergent yet
        else:
            return any([target1_found_left, target1_found_right, target1_found]), any([target2_found_left, target2_found_right, target2_found]), None
