# Given a traveler who travels a grid of size mxn ( m rows and n columns),
# find number of ways ( combination of moves) possible if the following constraints apply:
# Traveler at a given point is allowed to either go one step to the right or one step downwards
# Traveler starts in the top left corner and should travel to bottom right corner
# optimize using the tabulation method

def gridTravler(m, n):
    l = [[0 for i in range(n+1)] for j in range(m+1)]
    i = 0
    j = 0
    if i+ 1<= m and j+1 <=n:
        l[i+1][j+1] = 1
    for i in range(m +1):
        for j in range(n+1):
            if i + 1 <= m:
                l[i + 1][j] = l[i + 1][j] + l[i][j]
            if j + 1 <= n:
                l[i][j + 1] = l[i][j + 1] + l[i][j]

    return l[m][n]


if __name__ == '__main__':
    print(gridTravler(3, 3))
    print(gridTravler(0, 0))