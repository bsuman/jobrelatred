# You are given an m x n binary matrix grid.
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 on the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    numrows = len(grid)
    numcolumns = len(grid[0])
    isvistsed = [[False for _ in range(numcolumns)] for _ in range(numrows)]
    flist = []

    for i in range(numrows):
        for j in range(numcolumns):
            if not isvistsed[i][j]:
                if grid[i][j] == 1:
                    queue = [(i, j)]
                    tlist = []
                    while len(queue) > 0:
                        index = queue.pop(0)
                        r = index[0]
                        c = index[1]
                        if not isvistsed[r][c]:
                            isvistsed[r][c] = True
                            tlist.append(index)
                            if 0 <= r - 1 < numrows and grid[r - 1][c] == 1 and not isvistsed[r-1][c]:
                                queue.append((r - 1, c))
                            if 0 <= r + 1 < numrows and grid[r + 1][c] == 1 and not isvistsed[r+1][c]:
                                queue.append((r + 1, c))
                            if 0 <= c - 1 < numcolumns and grid[r][c - 1] == 1 and not isvistsed[r][c - 1]:
                                queue.append((r, c - 1))
                            if 0 <= c + 1 < numcolumns and grid[r][c + 1] == 1 and not isvistsed[r][c + 1]:
                                queue.append((r, c + 1))
                    flist.append(tlist)
                else:
                    isvistsed[i][j] = True

    max_area = 0
    for eachlist in flist:
        area = len(eachlist)
        if max_area < area:
            max_area = area

    return max_area


if __name__ == '__main__':
    # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(maxAreaOfIsland(grid))