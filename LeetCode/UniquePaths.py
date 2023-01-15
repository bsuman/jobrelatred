# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.


def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[m - 1][n - 1] = 1
    for j in range(n - 2, -1, -1):
        dp[m - 1][j] = 1

    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = 1

    for column in range(n - 2, -1, -1):
        for row in range(m-2, -1,-1):
            below = dp[row+1][column]
            right = dp[row][column+1]
            dp[row][column] = below + right

    return dp[0][0]


if __name__ == '__main__':
    print(uniquePaths(3,7))
    print(uniquePaths(3, 2))