# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    rows = len(mat)
    columns = len(mat[0])
    dlist = [[99999999 for _ in range(columns)] for _ in range(rows)]
    queue = []
    for i in range(rows):
        for j in range(columns):
            if mat[i][j] == 0:
                dlist[i][j] = 0
                queue.append((i, j))

    while len(queue):
        # l,r,t,b
        directions = [99999999] * 4
        index = queue.pop(0)
        i = index[0]
        j = index[1]
        top = i - 1
        bottom = i + 1
        left = j - 1
        right = j + 1
        if top >= 0 and dlist[top][j] == 99999999:
            dlist[top][j] = 1 + dlist[i][j]
            queue.append((top,j))
        if bottom < rows and dlist[bottom][j] == 99999999:
            dlist[bottom][j] = 1 + dlist[i][j]
            queue.append((bottom, j))
        if left >= 0 and dlist[i][left] == 99999999:
            dlist[i][left] = 1 + dlist[i][j]
            queue.append((i, left))
        if right < columns and dlist[i][right] == 99999999:
            dlist[i][right] = 1 + dlist[i][j]
            queue.append((i, right))

    return dlist


if __name__ == '__main__':
    # mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # print(updateMatrix(mat))
    mat = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]

    print(updateMatrix(mat))
