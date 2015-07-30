# store the number of incoming edges for every node
# put nodes with zero incoming edges on a stack
# start removing nodes with no imcoming edges from the graph, and put on output list
# for all nodes connected to the last removed node, decrement counts of incoming edges
# put new nodes with zero incoming edges on the stack
# repeat till 1) graph is empty or 2) stack is empty


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        num_incoming_nodes = [0] * numCourses
        graph = {}
        nodes_to_visit = []
        output = []

        for course, prereq in prerequisites:
            # prereq -> course
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
            # increment count
            num_incoming_nodes[course] += 1

        for course, in_degree in enumerate(num_incoming_nodes):
            if in_degree == 0:
                nodes_to_visit.append(course)

        while len(nodes_to_visit):
            current = nodes_to_visit.pop() # popping order does not matter
            for neighbor in graph.get(current, []):
                num_incoming_nodes[neighbor] -= 1
                if num_incoming_nodes[neighbor] == 0:
                    nodes_to_visit.append(neighbor)
            if current in graph:
                graph.pop(current)
            num_incoming_nodes[current] -= 1
            output.append(current)

        if len(graph) == 0:
            return output
        else:
            return []


            
