# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2)
# Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.num_rows = len(matrix)
        self.num_columns = len(matrix[0])
        self.dp = [[matrix[i][j] for j in range(self.num_columns)] for i in range(self.num_rows)]
        # sum row
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                self.dp[i][j] += (self.dp[i][j - 1] if j > 0 else 0)

        # sum column
        for j in range(self.num_columns):
            for i in range(self.num_rows):
                self.dp[i][j] += (self.dp[i - 1][j] if i > 0 else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1 = max(0, col1)
        x2 = min(self.num_columns - 1, col2)
        y1 = max(row1, 0)
        y2 = min(row2, self.num_rows - 1)
        t1 = self.dp[y2][x1 - 1] if x1 > 0 else 0
        t2 = self.dp[y1 - 1][x2] if y1 > 0 else 0
        t3 = self.dp[y1 - 1][x1 - 1] if (x1 > 0 and y1 > 0) else 0
        return self.dp[y2][x2] - t1 - t2 + t3


if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    row1, col1, row2, col2 = 2, 1, 4, 3
    print(obj.sumRegion(row1, col1, row2, col2))
    row1, col1, row2, col2 = 1, 1, 2, 2
    print(obj.sumRegion(row1, col1, row2, col2))