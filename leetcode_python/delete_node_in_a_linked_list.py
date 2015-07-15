# A linked list problem that doesn't involve pointer manipulation!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if not node:
            return

        while node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                return
            node = node.next
