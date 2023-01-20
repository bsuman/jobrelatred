# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

def makeGraph(numCourses, edges: list[list[int]]):
    graph = {}
    for i in range(numCourses):
        graph[i] = []

    for edge in edges:
        if edge[0] in graph.keys():
            graph[edge[0]] = graph[edge[0]] + [edge[1]]
    return graph


def iscycle(i, graph, visited, recstack):
    visited.add(i)
    recstack.add(i)
    for neighbour in graph[i]:
        if neighbour not in visited:
            if iscycle(neighbour, graph, visited, recstack):
                return True
        elif neighbour in recstack:
            return True
    recstack.remove(i)
    return False


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = makeGraph(numCourses, prerequisites)
    visited = set()
    recstack = set()
    for i in range(numCourses):
        if i not in visited:
            if iscycle(i, graph, visited, recstack):
                return False
    return True


if __name__ == '__main__':
    print(canFinish(2, [[1, 0], [0, 1]]))
