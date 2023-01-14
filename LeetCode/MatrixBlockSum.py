# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
# i - k <= r <= i + k,
# j - k <= c <= j + k
# (r, c) is a valid position in the matrix.

def matrixBlockSum(mat: list[list[int]], k: int) -> list[list[int]]:
    num_rows = len(mat)
    num_columns = len(mat[0])
    dp = [[mat[i][j] for j in range(num_columns)] for i in range(num_rows)]
    # sum row
    for i in range(num_rows):
        for j in range(num_columns):
            dp[i][j] += (dp[i][j - 1] if j > 0 else 0)

    # sum column
    for j in range(num_columns):
        for i in range(num_rows):
            dp[i][j] += (dp[i - 1][j] if i > 0 else 0)

    for i in range(num_rows):
        for j in range(num_columns):
            x1 = max(0, j - k)
            x2 = min(num_columns - 1, j + k)
            y1 = max(i - k, 0)
            y2 = min(i + k, num_rows - 1)
            t1 = dp[y2][x1 - 1] if x1 > 0 else 0
            t2 = dp[y1 - 1][x2] if y1 > 0 else 0
            t3 = dp[y1 - 1][x1 - 1] if (x1 > 0 and y1 > 0) else 0
            mat[i][j] = dp[y2][x2] - t1 - t2 + t3

    return mat


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(matrixBlockSum(mat, k))
