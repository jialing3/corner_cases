# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        for i in range(1, n):
            first = first.next
        second = dummy
        while first.next.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        
