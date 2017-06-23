from collections import defaultdict


class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance


def dijkstra_shortest_path(graph, start, offset=0):
  reached = {start: offset} # key is node, value is distance
  path = {} # key is destination_node, value is source_node

  unvisited = set(graph.nodes)

  while unvisited:
    candidates = unvisited.intersection(reached) # new nodes from last round
    if not candidates:
        break
    min_node = min(candidates, key=lambda x: reached[x])

    unvisited.remove(min_node)
    current_distance = reached[min_node]

    for edge in graph.edges[min_node]:
      distance = current_distance + graph.distances[(min_node, edge)]
      if edge not in reached or distance < reached[edge]:
        reached[edge] = distance
        path[edge] = min_node

  return reached, path


def get_path(path, end):
  output = []
  node = end
  while node:
      output = [node] + output
      node = path.get(node, None)
  return output
