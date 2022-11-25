# Given a traveler who travels a grid of size mxn ( m rows and n columns),
# find number of ways ( combination of moves) possible if the following constraints apply:
# Traveler at a given point is allowed to either go one step to the right or one step downwards
# Traveler starts in the top left corner and should travel to bottom right corner


def gridTraveler(m, n, d):
    key = str(m) + '_' + str(n)
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    elif key in d.keys():
        return d[key]
    else:
        d[key] = gridTraveler(m - 1, n,d) + gridTraveler(m, n - 1,d)
        revkey = str(n) + '_' + str(m) # ways of gridTraveler(m, n)  == ways of gridTraveler(n,m)
        d[revkey] = d[key]
        return d[key]

if __name__ == '__main__':
    d = {}
    print(gridTraveler(18, 18, d))