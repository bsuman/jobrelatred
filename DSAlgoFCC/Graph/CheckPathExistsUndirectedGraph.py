# given the edges of an undirected graph,source, destination, write a function to
# construct the graph and  to check if path exists

def checkifPathexists_bfs(source, destination, graph):
    queue = [source]
    visited_set = set()
    while len(queue) > 0:
        node = queue.pop()
        visited_set.add(node)
        if node == destination:
            return True
        if node in graph.keys():
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited_set:
                    queue.append(neighbor)

    return False


def checkifPathexists_dfs(source, destination, graph, visited_set):
    if source == destination:
        return True
    visited_set.add(source)
    if source in graph.keys():
        neighbors = graph[source]
        for neighbor in neighbors:
            if neighbor not in visited_set:
                if checkifPathexists_dfs(neighbor, destination, graph, visited_set):
                    return True
    return False


def createundirectedgraph(edges: list[list]):
    graph = {}
    for ilist in edges:
        node1 = ilist[0]
        node2 = ilist[1]
        if node1 in graph:
            graph[node1] = graph[node1] + [node2]
        else:
            graph[node1] = [node2]
        if node2 in graph:
            graph[node2] = graph[node2] + [node1]
        else:
            graph[node2] = [node1]

    return graph


if __name__ == '__main__':
    graph = createundirectedgraph([['i', 'j'], ['k', 'i'], ['k', 'j'], ['m', 'k'], ['k', 'l'], ['o', 'n']])
    print(graph)
    visited_set = set()
    print(checkifPathexists_dfs('k', 'i', graph,visited_set))
