# given a list of edges, create an undirected graph
# using the given source and destination, find the minimum distance path from source to destination

import CheckPathExistsUndirectedGraph as helper
import math


def minimumdistance(graph, source, destination) -> int:
    # each tuple indicates the node and distance of the node to the source
    queue = [(source, 0)]
    visited = set()
    while len(queue) > 0:
        info = queue.pop(0)
        node = info[0]
        distance = info[1]
        if node not in visited:
            visited.add(node)
            if node == destination:
                return distance
            else:
                if node in graph.keys():
                    neighbours = graph[node]
                    for neighbour in neighbours:
                        queue.append((neighbour, distance + 1))
    return -1


if __name__ == '__main__':
    graph = helper.createundirectedgraph([['w', 'x'], ['x', 'y'], ['z', 'y'], ['z', 'v'], ['w', 'v']])
    print(minimumdistance(graph, 'w', 'z'))
