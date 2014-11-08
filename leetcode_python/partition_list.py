# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        blue_head = ListNode(1)
        red_head = ListNode(2)
        blue_current = blue_head
        red_current = red_head
        current = head
        while current:
            next = current.next
            current.next = None
            if current.val < x:
                blue_current.next = current
                blue_current = blue_current.next
            else:
                red_current.next = current
                red_current = red_current.next
            current = next
        blue_current.next = red_head.next
        head = blue_head.next
        return head
