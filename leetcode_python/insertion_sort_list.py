# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insert(self, head, node):
        if head.val > node.val:
            node.next = head
            head = node
            return
        else:
            last = head
            current = head.next

        while True:
            if current is None:
                last.next = node
                node.next = None
                return
            elif current.val <= node.val:
                last = current
                current = current.next
                continue
            else:
                last.next = node
                node.next = current
                return

    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        last = head
        current = head.next
        while current:
            last.next = None
            next_node = current.next
            self.insert(head, current)
            last = current
            current = next_node
        return head
        
