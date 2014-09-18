# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 0     -> 1   -> 3 -> 4        -> 2   -> None
# dummy    pre         curr        tmp
#          1   -> 2 -> 3        -> 4   -> None
#          pre    tmp  pre.next    curr
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head

        dummy = ListNode(0) # add a dummy node to head
        dummy.next = head

        current = head
        while current.next:
            if current.next.val > current.val: # continue iteration if ascending
                current = current.next
            else:
                pre = dummy
                while pre.next.val < current.next.val: # move current.next to the right place
                    pre = pre.next
                tmp = current.next
                current.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp

        return dummy.next
