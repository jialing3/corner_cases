# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p_to_headA, p_to_headB = ListNode(0), ListNode(0)
        p_to_headA.next = headA
        p_to_headB.next = headB # handle zero and one-node cases

        len_A, len_B = 0, 0
        current_A, current_B = p_to_headA, p_to_headB
        while current_A.next:
            len_A += 1
            current_A = current_A.next
        while current_B.next:
            len_B += 1
            current_B = current_B.next

        current_A, current_B = p_to_headA, p_to_headB
        while current_A.next and current_B.next and current_A.next != current_B.next:
            if len_A > len_B:
                current_A = current_A.next
                len_A -= 1
            elif len_A < len_B:
                current_B = current_B.next
                len_B -= 1
            else:
                current_A = current_A.next
                len_A -= 1
                current_B = current_B.next
                len_B -= 1

        if not current_A.next or not current_B.next: # end reached
            return None
        else:
            return current_A.next # intersection found
