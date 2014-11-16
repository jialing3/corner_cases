# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        pointer_to_head = RandomListNode(0)
        current = head
        previous = pointer_to_head
        while current:
            tmp_copy = RandomListNode(current.label)
            current.mirror = tmp_copy
            previous.next = tmp_copy
            previous = tmp_copy
            current = current.next

        current = head
        tmp_copy = pointer_to_head.next
        while current:
            if current.random:
                tmp_copy.random = current.random.mirror
            current = current.next
            tmp_copy = tmp_copy.next
        return pointer_to_head.next
        
