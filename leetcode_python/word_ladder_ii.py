# Do breadth first search from both ends at the same time.
# Keep a set of all nodes that each has reached.
# When the sets have any element in common, there is a path.

# This is the most time-consuming leetcode problem I've seen so far, but the concepts touched have made this problem worthwhile.

class Solution:

    def get_next_nodes(self, node, dictionary, previous_nodes):
        next_nodes = []
        for i in range(len(node)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                tmp = node[:i] + c + node[i + 1:]
                if c != node[i] and tmp in dictionary and tmp not in previous_nodes:
                    next_nodes.append(tmp)
        return next_nodes

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dictionary): # dict is reserved and should not be used as parameter name
        start, end = end, start
        # elimination phase
        dictionary = set(dictionary)
        ends_met = False
        current_left = [start] # keep track of nodes at current level
        current_right = [end]
        left_nodes = set([start])
        right_nodes = set([end])
        while not ends_met and len(current_left) > 0 and len(current_right) > 0:
            past_left = current_left
            current_left = []
            past_right = current_right
            current_right = []
            for node in past_left:
                next_nodes = self.get_next_nodes(node, dictionary, left_nodes)
                for next_node in next_nodes:
                    current_left.append(next_node)
                    left_nodes.add(next_node)
            for node in past_right:
                next_nodes = self.get_next_nodes(node, dictionary, right_nodes)
                for next_node in next_nodes:
                    current_right.append(next_node)
                    right_nodes.add(next_node)
                    if next_node in left_nodes:
                        ends_met = True
        dictionary = left_nodes | right_nodes
        # solution finding phase
        connection_nodes = []
        ends_met = False
        current_left = [[start]] # keep track of paths
        current_right = [[end]]
        right_nodes = set([end])
        while not ends_met and len(current_left) > 0 and len(current_right) > 0:
            past_left = current_left
            current_left = []
            for path in past_left:
                next_nodes = self.get_next_nodes(path[-1], dictionary, set(path))
                for next_node in next_nodes:
                    current_left.append(path + [next_node])
                    if next_node in right_nodes:
                        ends_met = True
                        connection_nodes.append(next_node)
            if ends_met:
                break
            past_right = current_right
            current_right = []
            for path in past_right:
                next_nodes = self.get_next_nodes(path[-1], dictionary, set(path))
                for next_node in next_nodes:
                    current_right.append(path + [next_node])
                    right_nodes.add(next_node)
        to_return = []
        for left in current_left:
            if left[-1] in connection_nodes:
                for right in current_right:
                    if right[-1] == left[-1]:
                        to_return.append(left[:-1] + right[::-1])
        return [path[::-1] for path in to_return]
