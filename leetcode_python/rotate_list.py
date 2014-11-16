# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0: # edge len(Lined_List) <= 1, k == 0
            return head
        first = head
        for i in range(k):
            first = first.next
            if not first: # edge k > len(Linked_List)
                first = head
        if first == head: # edge k % len(Linked_List) == 0
            return head
        second = head
        while first:
            previous_to_first = first
            previous_to_second = second
            first = first.next
            second = second.next
        previous_to_first.next = head # original tail
        previous_to_second.next = None # new tail
        return second # new head
