# goal of the exercise to learn for loops in python
# implement a function which takes height of the christmas tree and draws the christmas tree

def getString(s, space):
    empty = " "
    for i in range(space):
        s = empty + s + empty
    print(s, "\n")


def drawChristmasTree(height):
    space = height - 1
    s = "x"
    first = True
    for i in range(height):
        if first:
            getString(s, space)
            first = False
        else:
            s = "x" + s + "x"
            getString(s, space)
        space = space - 1


if __name__ == '__main__':
    print("Please provide the height of the tree")
    drawChristmasTree(8)
