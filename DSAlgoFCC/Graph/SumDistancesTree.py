# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

def calculate_distance(source, graph, distance, rec_stack, destination) -> int:
    curr_distance = 0
    rec_stack.add(source)

    if source != destination and source in graph.keys():
        neighbours = graph[source]
        if (source, destination) in distance.keys():
            curr_distance = distance[(source, destination)]
        elif destination in neighbours:
            distance[(source, destination)] = 1
            distance[(destination, source)] = 1
            curr_distance = distance[(source, destination)]
        else:
            for neighbour in neighbours:
                if neighbour not in rec_stack:
                    curr_distance = calculate_distance(neighbour, graph, distance, rec_stack, destination)
                    if curr_distance != 0:
                        distance[(neighbour, destination)] = curr_distance
                        distance[(destination,neighbour)] = curr_distance
                        curr_distance = curr_distance + 1
                        break
    rec_stack.remove(source)
    return curr_distance


def sumOfDistancesInTree(n: int, edges: list[list[int]]) -> list[int]:
    graph = {}
    for node in edges:
        if node[0] not in graph.keys():
            graph[node[0]] = [node[1]]
        else:
            graph[node[0]] = graph[node[0]] + [node[1]]
        if node[1] not in graph.keys():
            graph[node[1]] = [node[0]]
        else:
            graph[node[1]] = graph[node[1]] + [node[0]]

    distance = {}
    answer = []
    rec_stack = set()
    for source in range(n):
        source_distance_sum = 0
        for destination in range(n):
            curr_distance = calculate_distance(source, graph, distance, rec_stack, destination)
            distance[(source, destination)] = curr_distance
            source_distance_sum += curr_distance
        answer.append(source_distance_sum)
    return answer


if __name__ == '__main__':
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(sumOfDistancesInTree(n, edges))
    n = 2
    edges = [[1, 0]]
    print(sumOfDistancesInTree(n, edges))
    n = 1
    edges = []
    print(sumOfDistancesInTree(n, edges))
