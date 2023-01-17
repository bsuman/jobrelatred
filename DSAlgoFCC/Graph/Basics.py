# Graph is stored as a dictionary with each node as the key and the connected nodes / edges as the value
# Access time O(1)
# Depth First Search implemented using the stack
# Breadth First Search implemented using the queue
def depthfirstsearch(node, graph):
    stack = [node]
    while len(stack) > 0:
        key = stack.pop(0)
        print('Node:', key)
        if key in graph.keys():
            val = graph[key]
            for i in val:
                stack.insert(0, i)


def rec_depthfirstsearch(node,graph):
    print('Node:', node)
    if node in graph.keys():
        val = graph[node]
        for i in val:
            rec_depthfirstsearch(i,graph)


def breadthfirstsearch(node,graph):
    queue = [node]
    while len(queue) > 0:
        key = queue.pop(0)
        print('Node:', key)
        if key in graph.keys():
            val = graph[key]
            for i in val:
                queue.append(i)


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': [],
        'e': [],
    }
    depthfirstsearch('a',graph)
    print("================================")
    breadthfirstsearch('a',graph)
    print("================================")
    rec_depthfirstsearch('a',graph)
