# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def findMid(self, head):
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None
        return mid

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        left, right = head, self.findMid(head)
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        merged = ListNode(0) # return merged.next
        current = merged
        while left is not None and right is not None:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        while left is not None:
            current.next = left
            left = left.next
            current = current.next
        while right is not None:
            current.next = right
            right = right.next
            current = current.next
        current.next = None
        return merged.next

    def sortList(self, head):
        return self.mergeSort(head)
