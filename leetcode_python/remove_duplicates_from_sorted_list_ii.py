# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p_to_head = ListNode(head.val - 1)
        p_to_head.next = head
        previous = p_to_head
        current = head
        while current:
            current.remove = False # base
            if previous.val == current.val:
                previous.remove = True
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        current = p_to_head.next
        previous = p_to_head
        while current:
            if current.remove:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return p_to_head.next
