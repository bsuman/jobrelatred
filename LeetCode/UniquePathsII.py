# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

def uniquePathsWithObstacles(obstacleGrid) -> int:
    num_rows = len(obstacleGrid)
    num_columns = len(obstacleGrid[0])
    dp = [[0 for j in range(num_columns)] for i in range(num_rows)]
    if obstacleGrid[num_rows - 1][num_columns - 1] == 0:
        dp[num_rows - 1][num_columns - 1] = 1
    else:
        return 0

    for j in range(num_columns - 2, -1, -1):
        if dp[num_rows - 1][j + 1] == 1 and obstacleGrid[num_rows - 1][j] != 1:
            dp[num_rows - 1][j] = 1

    for i in range(num_rows - 2, -1, -1):
        if dp[i + 1][num_columns - 1] == 1 and obstacleGrid[i][num_columns - 1] != 1:
            dp[i][num_columns - 1] = 1

    for column in range(num_columns - 2, -1, -1):
        for row in range(num_rows - 2, -1, -1):
            below = dp[row + 1][column]
            right = dp[row][column + 1]
            if obstacleGrid[row][column] != 1:
                dp[row][column] = below + right
    return dp[0][0]


if __name__ == '__main__':
    obstacleGrid =[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))
    obstacleGrid = [[0, 1], [0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))
