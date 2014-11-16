# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_second_to_last_node(self, head):
        previous = head
        while head.next:
            previous = head
            head = head.next
        return previous

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        empty_before_head = ListNode(0)
        empty_before_head.next = head
        previous_last = None
        while head:
            first = head
            second_to_last = self.find_second_to_last_node(head)
            last = second_to_last.next
            if first.next == last:
                head = None
            else:
                head = first.next
                second_to_last.next = None
            first.next = last
            if previous_last:
                previous_last.next = first
            previous_last = last
        return empty_before_head.next
        
