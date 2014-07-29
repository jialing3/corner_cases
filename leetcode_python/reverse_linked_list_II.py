# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):

        if m == n:
            return head

        counter = 1
        current = head

        while True:
            if not current is None:
                next = current.next

            if counter == m - 1:
                node_m_minus_1 = current
            elif counter == m:
                node_m = current
            elif counter == n:
                node_n = current
            elif counter == n + 1:
                node_n_plus_1 = current

            if (m + 1 <= counter <= n):
                current.next = previous

            if current is None:
                break

            counter += 1
            previous = current
            current = next

        if m != 1:
            node_m_minus_1.next = node_n
        else:
            head = node_n

        node_m.next = node_n_plus_1

        return head
