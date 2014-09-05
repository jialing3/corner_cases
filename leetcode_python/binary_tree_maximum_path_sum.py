'''
For root node, first check two subtrees and figure out
the path with maximum sum in each subtree (and the path
must contains the root node). More precisely, we can
compare root->val, root->val + leftsubtree, root->val
+ rightsubtree.

But this is not enough since the maximum path might
contains two subtrees. We have to compute the value
of root->val + leftsubtree + rightsubtree as well.
The problem is, we cannot directly return this value
since this path cannot go to upper nodes anymore. So
we also use another global variable to store the
maximum sum in each recursion, and update this variable
once we find any path with larger sum.
'''



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def max_at_node(self, node):
        '''returns max sum containing at most one subtree, and the sum containing at most two subtrees.'''
        if not node.left and not node.right: # no children
            return (node.val, node.val)
        if node.left:
            left, left_sum = self.max_at_node(node.left)
        if node.right:
            right, right_sum = self.max_at_node(node.right)
        if node.left and node.right: # has both children
            return (max([node.val, node.val + left, node.val + right]), max([node.val, node.val + left, node.val + right, node.val + left + right, left_sum, right_sum]))
        elif node.left: # has only left child
            return (max([node.val, node.val + left]), max([node.val, node.val + left, left_sum]))
        else: # has only right child
            return (max([node.val, node.val + right]), max([node.val, node.val + right, right_sum]))


    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        return self.max_at_node(root)[1]
