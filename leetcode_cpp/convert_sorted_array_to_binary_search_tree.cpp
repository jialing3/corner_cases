/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:

    TreeNode *sortedArrayToBST_helper(vector<int> &num, int start, int end) {
        if (start > end) return NULL; // important
        int n = (start + end) / 2;
        TreeNode *node = new TreeNode(num[n]);
        node -> left = sortedArrayToBST_helper(num, start, n - 1);
        node -> right = sortedArrayToBST_helper(num, n + 1, end);
        return node;
    }

    TreeNode *sortedArrayToBST(vector<int> &num) {
        return sortedArrayToBST_helper(num, 0, num.size() - 1);
    }
};
