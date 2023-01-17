# write a function connectedgraphcount that takes in the adjacency list of an undirected graph
# The function should return the number of connected components within the graph

import CheckPathExistsUndirectedGraph as helper


def connectedgraphcount(graph) -> int:
    visited = set()
    numcount = 0
    for key in graph.keys():
        if key not in visited:
            queue = [key]
            while len(queue) > 0:
                node = queue.pop()
                visited.add(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
            numcount += 1

    return numcount


if __name__ == '__main__':
    graph = helper.createundirectedgraph([[0, 8], [0, 1], [0, 5], [5, 8], [2, 3], [2, 4], [4, 3]])
    print(connectedgraphcount(graph))
    graph = helper.createundirectedgraph([[0, 8], [0, 1], [0, 5], [5, 8], [2, 3], [2, 4], [4, 3], [12, 13], [13, 14]])
    print(connectedgraphcount(graph))
