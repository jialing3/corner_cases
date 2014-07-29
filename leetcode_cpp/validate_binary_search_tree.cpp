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

    void inorder_traversal(TreeNode *node, vector<int>& vals) {
        if (node == NULL) {
            return;
        }
        inorder_traversal(node -> left, vals);
        vals.push_back(node -> val);
        inorder_traversal(node -> right, vals);
        return;
    }

    bool isValidBST(TreeNode *root) {
        // doing an in-order tree traversal should return an ordered list, and this can be used as a test for a valid BST

        vector<int> vals = {};
        inorder_traversal(root, vals);

        for (int i = 1; i < vals.size(); ++i) {
            if (vals[i - 1] >= vals[i]) {
                return false;
            }
        }
        return true;
    }
};
