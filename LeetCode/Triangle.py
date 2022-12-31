# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
def minimumTotal(triangle):
    n = len(triangle)
    dp = [[-1] * n for _ in range(n)]
    dp[n - 1] = triangle[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            lower_left = triangle[i][j] + dp[i + 1][j]
            lower_right = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(lower_left, lower_right)

    return dp[0][0]


if __name__ == '__main__':
    triangle = [[-1], [2, 3], [1, -1, -3]]
    print(minimumTotal(triangle))
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minimumTotal(triangle))
    triangle = [[-10]]
    print(minimumTotal(triangle))
