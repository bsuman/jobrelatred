def count_photos(road):
    # parse from left to right
    # for each right moving car check num cameras
    # for each right mobing cars number of photos taken will = num of cameras in it's path
    roadlist = list(road)
    numphotos = 0
    numright = 0
    numleft = 0
    right = '>'
    left = '<'
    camera = '.'
    l = len(roadlist)
    j = l - 1
    for i in range(l):
        if roadlist[i] == right:
            numright = numright + 1
        elif roadlist[i] == camera:
            numphotos = numphotos + numright

        if roadlist[j] == left:
            numleft = numleft + 1
        elif roadlist[j] == camera:
            numphotos = numphotos + numleft

        j = j - 1

    return numphotos

if __name__ == '__main__':
    res = count_photos(">.>..<" )
    print(res)