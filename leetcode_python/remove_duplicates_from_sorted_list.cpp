/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if (!head) {
            return head;
        }
        ListNode *previous = head, *current = head -> next;

        while(current) {
            if (current -> val == previous -> val) {
                current = current -> next;
                previous -> next = current;
            }
            else {
                previous = current;
                current = current -> next;
            }
        }

        return head;
    }
};
