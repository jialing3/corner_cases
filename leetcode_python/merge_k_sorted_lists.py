# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):

        nodes = [node for node in lists if node]
        nodes.sort(key=lambda x: x.val)

        node_to_head = ListNode(0)
        current = node_to_head

        while nodes:
            previous = current
            current = nodes.pop(0)
            previous.next = current

            if current.next:
                left, right = 0, len(nodes) - 1
                while left <= right:
                    mid = left + (right - left) / 2
                    if nodes[mid].val > current.next.val:
                        right = mid - 1
                    elif nodes[mid].val < current.next.val:
                        left = mid + 1
                    else:
                        left = mid
                        break
                nodes = nodes[:left] + [current.next] + nodes[left:]


        current.next = None
        return node_to_head.next


        
