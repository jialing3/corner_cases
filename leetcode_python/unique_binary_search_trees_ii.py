# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def generate_trees_recursive(self, num_list):
        if num_list in self.memo:
            return self.memo[num_list]
        else:
            if len(num_list) == 0:
                self.memo[num_list] = [None]
                return [None]
            elif len(num_list) == 1:
                tmp = TreeNode(num_list[0])
                self.memo[num_list] = [tmp]
                return [tmp]
            else:
                output = []
                for root in num_list:
                    left_nodes = self.generate_trees_recursive(filter(lambda x: x < root, num_list))
                    right_nodes = self.generate_trees_recursive(filter(lambda x: x > root, num_list))
                    for left in left_nodes:
                        for right in right_nodes:
                            tmp = TreeNode(root)
                            tmp.left = left
                            tmp.right =right
                            output.append(tmp)
                self.memo[num_list] = output
                return output

    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate_trees_recursive(tuple(range(1, n + 1)))
