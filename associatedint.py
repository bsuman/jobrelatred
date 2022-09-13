import numpy as np
import math


def factors(n, factorlist):
    i = 1
    increment = 2
    if n % 2 == 0:
        increment = 1
    lim = n / 2
    while i <= math.sqrt(n):
        quo = np.int(n // i)
        remain = np.int(n % i)
        if remain == 0:
            factorlist.append((np.int(i), quo))
            factorlist.append((quo, np.int(i)))
        i = i + increment


def area_value(n):
    if n == 1 or n == 0:
        return 0

    factorlist = []
    factors(int(n), factorlist)
    factorlist.sort()
    xlist = []
    ylist = []
    for i in factorlist:
        xlist.append(i[0])
        ylist.append(i[1])

    return np.int(np.trapz(ylist, x=xlist))