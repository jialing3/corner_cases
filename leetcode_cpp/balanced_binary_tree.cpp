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

    int getHeight(TreeNode *node) {
        if (!node) {
            return 0;
        }
        else if (!node -> left & !node -> right) {
            return 1;
        }
        int left = getHeight(node -> left), right = getHeight(node -> right);

        if (left == -1 | right == -1) {
            return -1;
        }
        else if (abs(left - right) <= 1) {
            return max(left, right) + 1;
        }
        else {
            return -1;
        }
    }

    bool isBalanced(TreeNode *root) {
        return !(getHeight(root) == -1);
    }
};
