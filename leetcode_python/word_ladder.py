class Solution:
    def get_next_nodes(self, node, dictionary, previous_nodes):
        next_nodes = []
        for i in range(len(node)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                tmp = node[:i] + c + node[i + 1:]
                if c != node[i] and tmp in dictionary and tmp not in previous_nodes:
                    next_nodes.append(tmp)
        return next_nodes


    def get_connection_nodes(self, start, end, dictionary):
        dictionary = set(dictionary)
        current_left = set([start]) # keep track of nodes at current level
        current_right = set([end])
        left_seen = set([start])
        right_seen = set([end])
        distance_left = 0
        distance_right = 0
        while len(current_left & current_right) == 0 and len(current_left) > 0 and len(current_right) > 0:
            past_left = current_left
            current_left = set()
            for node in past_left:
                next_nodes = self.get_next_nodes(node, dictionary, left_seen)
                for next_node in next_nodes:
                    current_left.add(next_node)
                    left_seen.add(next_node)
            distance_left += 1
            if len(current_left & current_right) > 0:
                break

            past_right = current_right
            current_right = set()
            for node in past_right:
                next_nodes = self.get_next_nodes(node, dictionary, right_seen)
                for next_node in next_nodes:
                    current_right.add(next_node)
                    right_seen.add(next_node)
            distance_right += 1

        return current_left & current_right, distance_left, distance_right


    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dictionary):
        connection_nodes, distance_left, distance_right = self.get_connection_nodes(start, end, dictionary)
        if len(connection_nodes) == 0:
            return 0
        else:
            return distance_left + distance_right + 1
