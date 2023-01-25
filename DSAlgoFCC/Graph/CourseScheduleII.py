# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses.
# If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.

def isCycle(source, graph, visited, rec_stack, order_list):
    visited.add(source)
    rec_stack.add(source)
    for neighbor in graph[source]:
        if neighbor not in visited:
            if isCycle(neighbor, graph, visited, rec_stack,order_list):
                return True
        elif neighbor in rec_stack:
            return True
    rec_stack.remove(source)
    order_list.append(source)
    return False


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {}
    for num in range(numCourses):
        graph[num] = []

    for edge in prerequisites:
        graph[edge[0]].append(edge[1])

    visited = set()
    rec_stack = set()
    order_list = []
    for course in range(numCourses):
        if course not in visited:
            if isCycle(course, graph, visited, rec_stack,order_list):
                return []
    return order_list


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[0,1]]
    print(findOrder(numCourses, prerequisites))
    numCourses = 2
    prerequisites = [[1, 0]]
    print(findOrder(numCourses, prerequisites))
    numCourses = 1
    prerequisites = []
    print(findOrder(numCourses, prerequisites))
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(findOrder(numCourses, prerequisites))