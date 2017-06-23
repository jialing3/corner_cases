#!/usr/local/bin/python3
'''
use Dijkstra's shortest path per suggestion from @osullisg
'''

from dijkstra import Graph, dijkstra_shortest_path, get_path

sample_data = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]

data = []

with open('p083_matrix.txt') as f:
    for line in f.readlines():
        line = list(map(int, line.strip().split(',')))
        data.append(line)


def get_neighbors(data, i, j):
    neighbor_locs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(m, n) for m, n in neighbor_locs
                   if 0 <= m < len(data) and
                      0 <= n < len(data[0])]


def load_graph(data):
    g = Graph()
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            g.add_node(str(i) + '_' + str(j))
            for m, n in get_neighbors(data, i, j):
                g.add_edge(str(m) + '_' + str(n), str(i) + '_' + str(j), data[i][j])
    return g

sample_g = load_graph(sample_data)
sample_distances, sample_path = dijkstra_shortest_path(sample_g, '0_0', sample_data[0][0])
print(get_path(sample_path, '4_4'))
print(sample_distances['4_4'])

g = load_graph(data)
distances, path = dijkstra_shortest_path(g, '0_0', data[0][0])
print(get_path(path, '79_79'))
print(distances['79_79'])
