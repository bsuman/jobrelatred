# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

import math


def minFallingPathSum(matrix: list[list[int]]) -> int:
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    for i in range(1, num_rows):
        for j in range(1, num_columns - 1):
            matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i - 1][j + 1])
        matrix[i][0] = matrix[i][0] + min(matrix[i-1][0],matrix[i-1][1])
        matrix[i][num_columns-1] = matrix[i][num_columns-1] + min(matrix[i - 1][num_columns-2], matrix[i - 1][num_columns-1])

    return min(matrix[num_rows-1])


if __name__ == '__main__':
    matrix = [[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]
    print(minFallingPathSum(matrix))
    matrix = [[-19, 57], [-40, -5]]
    print(minFallingPathSum(matrix))
