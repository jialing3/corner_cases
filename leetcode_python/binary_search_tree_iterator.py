# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.nodes_to_visit = []
        self.push_left(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.nodes_to_visit)

    # @return an integer, the next smallest number
    def next(self):
        current = self.nodes_to_visit.pop()
        if current.right:
            self.push_left(current.right)
        return current.val

    def push_left(self, node):
        while node:
            self.nodes_to_visit.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
