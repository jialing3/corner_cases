# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return None
        carry = 0
        pointer_to_l3 = ListNode(0)
        current = pointer_to_l3
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            tmp_sum = l1.val + l2.val + carry # don't forget
            carry = tmp_sum / 10
            l3 = ListNode(tmp_sum % 10)
            current.next = l3
            l1 = l1.next
            l2 = l2.next
            current = current.next
        # key! biggest carry-over digit
        if carry:
            current.next = ListNode(carry)
        return pointer_to_l3.next
        
