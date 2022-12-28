# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

def orangesRotting(grid) -> int:
    rows = len(grid)
    columns = len(grid[0])
    queue = []
    num_fresh_oranges = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                num_fresh_oranges = num_fresh_oranges + 1

    if num_fresh_oranges == 0:
        return 0
    # no rotten oranges in the grid
    elif len(queue) == 0:
        return -1
    elif len(queue) == (rows * columns):
        return 0

    num_min = 0
    num_len = len(queue)
    while num_len > 0:
        tmp_queue = []
        for i in range(num_len):
            index = queue.pop(0)
            i = index[0]
            j = index[1]
            top = i - 1
            bottom = i + 1
            left = j - 1
            right = j + 1
            if top >= 0 and grid[top][j] == 1:
                grid[top][j] = 2
                num_fresh_oranges = num_fresh_oranges - 1
                tmp_queue.append((top, j))
            if bottom < rows and grid[bottom][j] == 1:
                grid[bottom][j] = 2
                num_fresh_oranges = num_fresh_oranges - 1
                tmp_queue.append((bottom, j))
            if left >= 0 and grid[i][left] == 1:
                grid[i][left] = 2
                num_fresh_oranges = num_fresh_oranges - 1
                tmp_queue.append((i, left))
            if right < columns and grid[i][right] == 1:
                grid[i][right] = 2
                num_fresh_oranges = num_fresh_oranges - 1
                tmp_queue.append((i, right))

        num_len = len(tmp_queue)
        if num_len > 0:
            queue = tmp_queue
            num_min = num_min + 1

    if num_fresh_oranges == 0:
        return num_min
    else:
        return -1


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(orangesRotting(grid))
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(orangesRotting(grid))
    grid = [[0, 2]]
    print(orangesRotting(grid))
