# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root: # edge
            return []
        current = [root]
        output = []
        counter = 0
        while len(current):
            if counter % 2 == 0:
                output.append([node.val for node in current])
            else:
                output.append([node.val for node in reversed(current)])
            next_ = []
            for node in current:
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            current = next_
            counter += 1
        return output
