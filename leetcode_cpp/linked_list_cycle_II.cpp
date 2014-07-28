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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        ListNode *slow = head -> next;
        ListNode *fast = head -> next -> next;
        ListNode *third = head;
        while (fast != NULL) {
            if (slow == fast) {
                while (third != slow) {
                    third = third -> next;
                    slow = slow -> next;
                }
                return slow;
            }
            if (fast -> next == NULL) {
                return NULL;
            }
            slow = slow -> next;
            fast = fast -> next;
        }
        return NULL;
    }
};
