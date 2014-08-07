# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            one, two, three = head, head.next, head.next.next
            head = two
            two.next = one # relink
        while True:
            if three is None or three.next is None:
                one.next = three
                return head
            else:
                four, five = three.next, three.next.next
                one.next = four # relink
                four.next = three # relink
                one, three = three, five


            
