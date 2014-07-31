# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        previous, current = head, head.next
        while (current):
            if current.val == previous.val:
                current = current.next
                previous.next = current
            else:
                previous, current = current, current.next
        return head
