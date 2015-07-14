# best pointer arithmetic exercise

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        ptr_to_head = ListNode(0)
        ptr_to_head.next = head

        node_before = ptr_to_head
        current = head
        cnt = 0

        while current:
            cnt += 1
            if cnt % k == 0:
                node_after = current.next
                node_before = self.reverse_nodes(node_before, node_after)
                current = node_before.next
            else:
                current = current.next

        return ptr_to_head.next


    def reverse_nodes(self, node_before, node_after): # reverse the nodes in-between
        # node_before -> [prev -> curr] x (k - 1) -> node_after
        # the first prev would be the new node_before
        # fix the first and last linkages
        prev = node_before.next
        new_node_before = prev
        curr = prev.next
        while curr != node_after:
            new_curr = curr.next
            curr.next = prev
            prev = curr
            curr = new_curr
        node_before.next = prev
        new_node_before.next = node_after
        return new_node_before
