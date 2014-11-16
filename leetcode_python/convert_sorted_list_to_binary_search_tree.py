# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_mid_element(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        return previous # the previous element of None: None, 1: 0th, 2: 1st, 3: 1st, 4: 2nd, etc

    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        previous_to_mid = self.get_mid_element(head)
        mid = previous_to_mid.next
        left, right = head, mid.next
        previous_to_mid.next = None # terminate left half of the list
        root_node = TreeNode(mid.val)
        root_node.left = self.sortedListToBST(left)
        root_node.right = self.sortedListToBST(right)
        return root_node
