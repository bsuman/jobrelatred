# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


def numIslands(grid) -> int:
    num_rows = len(grid)
    num_columns = len(grid[0])
    visited = [[False for _ in range(num_columns)] for _ in range(num_rows)]
    queue = []
    num_island = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if not visited[i][j] and grid[i][j] == "1":
                queue.append((i, j))
                num_island += 1
                while len(queue) > 0:
                    (row, column) = queue.pop(0)
                    if not visited[row][column]:
                        visited[row][column] = True
                        # north direction
                        if row - 1 >= 0 and not visited[row - 1][column] and grid[row - 1][column] == "1":
                            queue.append((row - 1, column))
                        # south direction
                        if row + 1 < num_rows and not visited[row + 1][column] and grid[row + 1][column] == "1":
                            queue.append((row + 1, column))
                        # left direction
                        if column - 1 >= 0 and not visited[row][column - 1] and grid[row][column - 1] == "1":
                            queue.append((row, column - 1))
                        # right direction
                        if column + 1 < num_columns and not visited[row][column + 1] and grid[row][column + 1] == "1":
                            queue.append((row, column + 1))

    return num_island


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(numIslands(grid))
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(numIslands(grid))