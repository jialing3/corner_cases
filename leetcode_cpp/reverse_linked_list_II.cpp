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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        // case in which no swap is needed
        if (m == n) {
            return head;
        }

        ListNode *current = head;
        ListNode *next;
        ListNode *previous;
        int counter = 1;
        ListNode *node_m_minus_1;
        ListNode *node_m;
        ListNode *node_n;
        ListNode *node_n_plus_1;


        // case in which swap starts from the beginning
        while (true) {
            if (current != NULL) {
                next = current -> next;
            }

            if (counter == m - 1) {
                node_m_minus_1 = current;
            }
            else if (counter == m) {
                node_m = current;
            }
            else if (counter == n) {
                node_n = current;
            }
            else if (counter == n + 1) {
                node_n_plus_1 = current;
            }

            if (counter >= m + 1 && counter <= n) {
                current -> next = previous;
            }

            if (current == NULL) {
                break;
            }

            counter += 1;
            previous = current;
            current = next;
        }

        if (m != 1) {
            node_m_minus_1 -> next = node_n;
        }
        else {
            head = node_n;
        }
        node_m -> next = node_n_plus_1;

        return head;
    }
};
