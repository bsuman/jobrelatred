def eatfish(mysize, threshold, mylist):
    eatsize = 0
    #if threshold < mysize:
        #eatsize = threshold
    #else:
    eatsize = mysize

    if eatsize > 9:
        eatsize = 9

    while eatsize > 0:
        if mylist[eatsize] > 0:
            mylist[eatsize] = mylist[eatsize] -1
            return eatsize
        eatsize = eatsize - 1
    return 0


def eatallfish(mylist, edible):
    mysize = 1
    threshold = 4 * mysize
    fishtoeat= True
    while fishtoeat:
        eatsize = eatfish(mysize, threshold, mylist)
        if eatsize == 0:
            return mysize
        threshold = threshold - eatsize
        if threshold <= 0:
            mysize = mysize + 1
            threshold = 4 * mysize + threshold




def fish(shoal):
    length = len(shoal)
    print(length)
    mysize = 1
    if length == 0 or length == 1:
        return mysize
    else:
        mylist = {}
        for i in range(1,10):
            mylist[i] = shoal.count(str(i))
        print(mylist)
        edible = mysize
        mysize = eatallfish(mylist, edible)
    return mysize


if __name__ == '__main__':
    ms = fish("274457805181503095015137244433301704602597113631474794519")
    #ms =fish("111111111111111111112222222222")
    print(ms)
