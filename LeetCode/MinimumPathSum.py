# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


def minPathSum(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_columns = len(grid[0])
    dp = [[0 for j in range(num_columns)] for i in range(num_rows)]
    dp[num_rows - 1][num_columns - 1] = grid[num_rows - 1][num_columns - 1]

    for j in range(num_columns - 2, -1, -1):
        dp[num_rows - 1][j] = dp[num_rows - 1][j + 1] + grid[num_rows - 1][j]

    for i in range(num_rows - 2, -1, -1):
        dp[i][num_columns - 1] = dp[i + 1][num_columns - 1] + grid[i][num_columns - 1]

    for column in range(num_columns - 2, -1, -1):
        for row in range(num_rows - 2, -1, -1):
            below = dp[row + 1][column]
            right = dp[row][column + 1]
            dp[row][column] = min(below, right) + grid[row][column]

    return dp[0][0]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))
