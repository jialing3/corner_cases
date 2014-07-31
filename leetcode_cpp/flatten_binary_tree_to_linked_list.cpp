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

    TreeNode* pre_order(TreeNode *node, TreeNode *previous) {

        // remember the daughters
        TreeNode* remember_left = (node -> left != NULL) ? node -> left : NULL;
        TreeNode* remember_right = (node -> right != NULL) ? node -> right : NULL;

        // rewire
        if (previous != NULL) {
            previous -> right = node;
            previous -> left = NULL;
        }

        TreeNode* left = NULL;
        TreeNode* right = NULL;

        // recurse
        if (remember_left)
            left = pre_order(remember_left, node);
        if (remember_right)
            right = pre_order(remember_right, (remember_left) ? left : node);

        // return previous for the next step of traversal
        if (remember_right) {
            return right;
        }
        else if (remember_left) {
            return left;
        }
        else {
            return node;
        }
    }

    void flatten(TreeNode *root) {

        if (root == NULL) {
            return;
        }

        pre_order(root, NULL);

    }
};
