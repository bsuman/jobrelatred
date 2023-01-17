# if given a source and destination for given acyclic graph, check if path exists

def checkifPathExists_DFS(source, destination, graph):
    stack = [source]
    while len(stack):
        node = stack.pop(0)
        if node == destination:
            return True
        if node in graph.keys():
            values = graph[node]
            for val in values:
                stack.insert(0, val)
    return False


def checkifPathExists_BFS(source, destination, graph):
    queue = [source]
    while len(queue):
        node = queue.pop(0)
        if node == destination:
            return True
        if node in graph.keys():
            values = graph[node]
            for val in values:
                queue.append(val)
    return False


if __name__ == '__main__':
    graph = {
        'f': ['i', 'g'],
        'i': ['g', 'k'],
        'g': ['h'],
        'h': [],
        'j': ['i'],
        'k': []
    }
    print(checkifPathExists_DFS('f', 'k', graph))
    print(checkifPathExists_DFS('f', 'h', graph))
    print(checkifPathExists_DFS('g', 'j', graph))
    print(checkifPathExists_BFS('f', 'k', graph))
    print(checkifPathExists_BFS('f', 'h', graph))
    print(checkifPathExists_BFS('g', 'j', graph))
