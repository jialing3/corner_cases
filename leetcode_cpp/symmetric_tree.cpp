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
    bool isMirror(TreeNode *left, TreeNode *right) {
        if (!left and !right) return true;
        else if (!left) return false;
        else if (!right) return false;

        if (left -> val != right -> val) {
            return false;
        }
        else if (!isMirror(left -> left, right -> right)) {
            return false;
        }
        else return isMirror(left -> right, right -> left);
    }

    bool isSymmetric(TreeNode *root) {
        if (!root) return true;
        return isMirror(root -> left, root -> right);
    }
};
