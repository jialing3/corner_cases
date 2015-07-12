# reverse the first half of the list and compare with the second half

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # break list down from the middle
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next is None: # even
            new_head = slow.next
            slow.next = None
        else: # odd, fast.next.next is None
            new_head = slow.next.next
            slow.next = None

        # reverse the first half
        node = head
        last = None
        while node:
            next__ = node.next
            node.next = last
            last = node
            node = next__

        # compare
        node1 = last
        node2 = new_head
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
        
