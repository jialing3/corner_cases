# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while fast:
            if slow == fast:
                third = head
                while third != slow:
                    third = third.next
                    slow = slow.next
                return slow
            if fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        return None
