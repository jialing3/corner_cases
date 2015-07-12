# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.reverse(None, head)


    def reverse(self, last, current):
        if current is None:
            return last
        elif current.next is None:
            current.next = last
            return current
        else:
            new_head = self.reverse(current, current.next)
            current.next.next = current
            current.next = last
            return new_head

        
