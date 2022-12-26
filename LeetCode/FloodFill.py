# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel,
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
# Replace the color of all the aforementioned pixels with color.
# Return the modified image after performing the flood fill.


# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n


def floodFill(image: list[list[int]], sr: int, sc: int, color: int):
    # get the row length
    row = len(image)
    # get the column length
    column = len(image[0])
    # append the start index
    queue = [(sr, sc)]
    # variable to store color relevant to find the relevant neighbors
    srcolor = None

    # process until no more indexes left
    while len(queue) > 0:
        # pop the first element in the queue to process
        index = queue.pop(0)
        # if current index is the target index
        if index[0] == sr and index[1] == sc:
            # if the target index is of the target color, do nothing
            if image[index[0]][index[1]] == color:
                break
            else:
                # if the target index  is not of the target color, save the relevant source color to find the relevant neighbors
                srcolor = image[index[0]][index[1]]

        # update the target index with the new color
        image[index[0]][index[1]] = color
        # check the bottom direction if in range
        if 0 <= index[0] - 1 < row and image[index[0] - 1][index[1]] == srcolor:
            image[index[0] - 1][index[1]] = color
            queue.append((index[0] - 1, index[1]))
        # check the top direction if in range
        if 0 <= index[0] + 1 < row and image[index[0] + 1][index[1]] == srcolor:
            image[index[0] + 1][index[1]] = color
            queue.append((index[0] + 1, index[1]))
        # check the left direction if in range
        if 0 <= index[1] - 1 < column and image[index[0]][index[1] - 1] == srcolor:
            image[index[0]][index[1] - 1] = color
            queue.append((index[0], index[1] - 1))
        # check the right direction if in range
        if 0 <= index[1] + 1 < column and image[index[0]][index[1] + 1] == srcolor:
            image[index[0]][index[1] + 1] = color
            queue.append((index[0], index[1] + 1))

    return image


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(image, sr, sc, color))
