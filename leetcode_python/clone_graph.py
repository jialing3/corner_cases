# BFS

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        nodes_to_visit = {node: None}
        nodes_seen = set()
        cnt = 0
        while len(nodes_to_visit) > 0:
            new_nodes = {}
            current_nodes_copied = []
            for node in nodes_to_visit.iterkeys():
                tmp_node = UndirectedGraphNode(node.label)
                current_nodes_copied.append(tmp_node)
                if cnt == 0:
                    output_node = tmp_node
                if nodes_to_visit[node]:
                    nodes_to_visit[node].neighbors.append(tmp_node)
                for neighbor in node.neighbors:
                    if neighbor not in nodes_seen:
                        new_nodes[neighbor] = tmp_node # copied source node
                        nodes_seen.add(neighbor)
                    elif neighbor == node:
                        tmp_node.neighbors.append(tmp_node)
                cnt += 1
            # same-level connection
            for node_ind, node in enumerate(nodes_to_visit.iterkeys()):
                for neighbor in node.neighbors:
                    if neighbor in nodes_to_visit:
                        neighbor_copied = current_nodes_copied[nodes_to_visit.keys().index(neighbor)]
                        current_nodes_copied[node_ind].neighbors.append(neighbor_copied)
            nodes_to_visit = new_nodes
        return output_node

        
