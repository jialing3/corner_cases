# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def make_double_link(self, head):
        previous = head
        current = head.next
        while current:
            current.last = previous
            previous = current
            current = current.next
        return previous

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head
        pointer_to_head = ListNode(0)
        pointer_to_head.next = head
        tail = self.make_double_link(pointer_to_head)
        previous_right = None
        while tail.next != head.last and tail.next != head: # notice the two-element and three-element cases
            left = head
            right = tail
            head = head.next
            tail = tail.last
            left.next = right
            right.next = None
            if previous_right:
                previous_right.next = left
            previous_right = right
        return pointer_to_head.next
