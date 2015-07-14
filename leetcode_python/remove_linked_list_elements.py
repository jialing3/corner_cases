# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        ptr_to_head = ListNode(0)
        ptr_to_head.next = head

        current = ptr_to_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return ptr_to_head.next
