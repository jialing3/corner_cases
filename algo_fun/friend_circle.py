class Solution:
    def dfs(self, root, adjacency_matrix, nodes_visited):
        nodes_to_visit = [root]

        while nodes_to_visit:
            current = nodes_to_visit.pop()
            nodes_visited.add(current)
            for person, is_friend in enumerate(adjacency_matrix[current]):
                if person not in nodes_visited and is_friend == 'y':
                    nodes_to_visit.append(person)

        return

    def get_num_of_circles(self, adjacency_matrix):
        adjacency_matrix = [list(_) for _ in adjacency_matrix]
        num_of_people = len(adjacency_matrix)
        cnt = 0
        nodes_visited = set()

        for person in range(len(adjacency_matrix)):
            if person not in nodes_visited:
                self.dfs(person, adjacency_matrix, nodes_visited)
                cnt += 1

        return cnt

if __name__ == '__main__':
    sol = Solution()
    adjacency_matrix_1 = ['ynyynnn',
                          'nyynnnn',
                          'yyynnnn',
                          'ynnynnn',
                          'nnnnyyn',
                          'nnnnyyn',
                          'nnnnnny']
    print(sol.get_num_of_circles(adjacency_matrix_1))
