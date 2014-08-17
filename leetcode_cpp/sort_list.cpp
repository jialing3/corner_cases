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
    ListNode *findMid(ListNode *head) {
        ListNode *slow = head, *fast = head, *mid;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        mid = slow->next;
        slow->next = NULL;
        return mid;
    }

    ListNode *mergeSort(ListNode *head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode *left = head, *right = findMid(head);
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }

    ListNode *merge(ListNode *left, ListNode *right) {
        ListNode *merged = new ListNode(0); // new
        ListNode *current = merged; // return merged->next
        while (left && right) {
            if (left->val < right->val) {
                current->next = left;
                left = left->next;
            }
            else {
                current->next = right;
                right = right->next;
            }
            current = current->next;
        }
        while (left) {
            current->next = left;
            left = left->next;
            current = current->next;
        }
        while (right) {
            current->next = right;
            right = right->next;
            current = current->next;
        }
        current->next = NULL;
        return merged->next;
    }

    ListNode *sortList(ListNode *head) {
        return mergeSort(head);
    }
};
