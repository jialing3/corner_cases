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
    ListNode *swapPairs(ListNode *head) {
        if (!head || !head -> next) {
            return head;
        }

        ListNode *one = head, *two = head -> next, *three = head -> next -> next;
        head = two;
        two -> next = one;

        while (true) {
            if (!three || !three -> next) {
                one -> next = three;
                return head;
            }
            else {
                ListNode *four = three -> next, *five = three -> next -> next;
                one -> next = four;
                four -> next = three;
                one = three;
                three = five;
            }
        }
    }
};
