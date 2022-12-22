def dochecks(maze, row, column, endindex, columnindex, rowindex):
    if 0 <= rowindex < row and 0 <= columnindex < column:
        if maze[rowindex][columnindex] == 1:
            return 'Dead'
        elif rowindex == endindex[0] and columnindex == endindex[1]:
            return 'Finish'
        elif maze[rowindex][columnindex] == 0 or maze[rowindex][columnindex] == 2:
            return 'Safe'
    else:
        return 'Dead'

def maze_runner(maze, directions):
    row = len(maze)
    column = len(maze)
    startindex = (-1, -1)
    endindex = (-1, -1)
    start = 2
    end = 3
    #print(directions)
    #print(maze)
    for i in range(row):
        if start in maze[i]:
            found = maze[i].index(start)
            if found != -1:
                startindex = (i, found)

        if end in maze[i]:
            found = maze[i].index(end)
            if found != -1:
                endindex = (i, found)

    totalmoves = len(directions)
    currentmove = 0
    rowindex = startindex[0]
    columnindex = startindex[1]

    retval = 0
    while currentmove < totalmoves:
        move = directions[currentmove]
        if move == "N":
            rowindex = rowindex - 1
        elif move == "S":
            rowindex = rowindex + 1
        elif move == "E":
            columnindex = columnindex + 1
        elif move == "W":
            columnindex = columnindex - 1

        retval = dochecks(maze, row, column, endindex, columnindex, rowindex)
        if retval == 'Finish':
            return 'Finish'
        elif retval == 'Dead':
            return 'Dead'
        elif retval == 'Safe':
            currentmove = currentmove + 1

    return 'Lost'


if __name__ == '__main__':
    #maze = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]]

    #maze = [[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            #[1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
            #[1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            #[1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            #[1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            #[1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            #[1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            #[1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            #[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            #[1, 1, 1, 0, 1, 1, 1, 1, 2, 1]]

    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]]

    retval = maze_runner(maze, ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']) #"Lost"
    print(retval)