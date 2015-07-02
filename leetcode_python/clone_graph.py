'''
clone_map = {original_node: cloned_node}
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        clone_map = {} # double as visited set
        stack = []
        if node:
            stack.append(node)
            clone_map[node] = UndirectedGraphNode(node.label)
        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                # important, even if the neighbor is already cloned, still need to check linkage
                clone_map[current].neighbors.append(clone_map[neighbor])

        return clone_map.get(node, None)

    def BFS(self, node):
        queue = []
        visited = set()
        if node:
            queue.append(node)
            visited.add(node)
        while queue:
            current = queue.pop(0) # O[n], FIFO
            print current.label
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return

    def DFS(self, node):
        stack = []
        visited = set()
        if node:
            stack.append(node)
            visited.add(node)
        while stack:
            current = stack.pop() # FILO
            print current.label
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return



if __name__ == '__main__':
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node4 = UndirectedGraphNode(4)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node4]
    node3.neighbors = [node1]

    sol = Solution()
    sol.BFS(node1) # 1, 2, 3
    sol.DFS(node1) # 1, 3, 2
