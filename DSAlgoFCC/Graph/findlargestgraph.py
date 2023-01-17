# write a function largestgraphsize that takes in the adjacency list of an undirected graph.
# The function should return the size of the largest connected graph within the list.
import CheckPathExistsUndirectedGraph as helper


def largestgraphsize(graph) -> int:
    visited = set()
    max_size = 0
    for key in graph.keys():
        if key not in visited:
            queue = [key]
            visited.add(key)
            curr_size = 0
            while len(queue) > 0:
                node = queue.pop()
                curr_size = curr_size + 1
                neighbours = graph[node]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            if max_size < curr_size:
                max_size = curr_size

    return max_size


if __name__ == '__main__':
    graph = helper.createundirectedgraph([[0, 8], [0, 1], [0, 5], [5, 8], [2, 3], [2, 4], [4, 3]])
    print(largestgraphsize(graph))
    graph = helper.createundirectedgraph(
        [[0, 8], [0, 1], [0, 5], [5, 8], [8, 9], [2, 3], [2, 4], [4, 3], [12, 13], [13, 14]])
    print(largestgraphsize(graph))
