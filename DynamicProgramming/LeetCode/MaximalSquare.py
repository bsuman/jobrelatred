# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

def maximalSquare(matrix: list[list[str]]) -> int:
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    dp = [[0 for j in range(num_columns)] for i in range(num_rows)]
    dp[num_rows - 1][num_columns - 1] = int(matrix[num_rows - 1][num_columns - 1])

    for j in range(num_columns - 2, -1, -1):
        dp[num_rows - 1][j] = int(matrix[num_rows - 1][j])

    for i in range(num_rows - 2, -1, -1):
        dp[i][num_columns - 1] = int(matrix[i][num_columns - 1])

    max_len = 0
    for column in range(num_columns - 2, -1, -1):
        for row in range(num_rows - 2, -1, -1):
            if matrix[row][column] == "1":
                below = dp[row + 1][column]
                right = dp[row][column + 1]
                diagonal = dp[row + 1][column + 1]
                dp[row][column] = 1 + min(below, right, diagonal)

    for row in range(0, num_rows):
        for column in range(0, num_columns):
            if max_len < dp[row][column]:
                max_len = dp[row][column]

    return max_len * max_len


if __name__ == '__main__':
    print(maximalSquare([["0","1"],["1","0"]]))
    print(maximalSquare([["0"]]))
    print(maximalSquare(
        [("1", "0", "1", "0", "0"), ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
