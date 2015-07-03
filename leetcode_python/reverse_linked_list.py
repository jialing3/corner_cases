# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        last = None
        current = head
        while current:
            current_next = current.next # memorize for current = current_next
            current.next = last
            last = current
            current = current_next
        return last
        
