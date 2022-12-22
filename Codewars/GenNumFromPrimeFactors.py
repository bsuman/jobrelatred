# Given a list of prime factors, primesL, and an integer, limit, try to generate in order,
# all the numbers less than the value of limit, that have all and only the prime factors of primesL
#
# Example
# primesL = [2, 5, 7]
# limit = 500
# List of Numbers Under 500          Prime Factorization
# ___________________________________________________________
#            70                         [2, 5, 7]
#           140                         [2, 2, 5, 7]
#           280                         [2, 2, 2, 5, 7]
#           350                         [2, 5, 5, 7]
#           490                         [2, 5, 7, 7]
# There are 5 of these numbers under 500 and the largest one is 490.
#
# Task
# For this kata you have to create the function count_find_num(), that accepts two arguments:
# primesL and limit, and returns the amount of numbers that fulfill the requirements, and the largest number under limit.
#
# The example given above will be:
#
# primesL = [2, 5, 7]
# limit = 500
# count_find_num(primesL, val) == [5, 490]
# If no numbers can be generated under limit then return an empty list:
#
# primesL = [2, 3, 47]
# limit = 200
# find_nums(primesL, limit) == []
# The result should consider the limit as inclusive:
#
# primesL = [2, 3, 47]
# limit = 282
# find_nums(primesL, limit) == [1, 282]
# Features of the random tests:
#
# number of tests = 200
# 2 <= length_primesL <= 6 // length of the given prime factors array
# 5000 <= limit <= 1e17
# 2 <= prime <= 499  // for every prime in primesL

import numpy

def multiplyfactors(prod,primesL, limit, count, maxprod, processedNum):
    for i in primesL:
        newprod = prod * i
        if newprod <= limit and newprod not in processedNum:
            count = count + 1
            processedNum.append(newprod)
            if newprod > maxprod:
                maxprod = newprod
            cnt, mprod = multiplyfactors(newprod,primesL, limit, count, maxprod,processedNum)
            count = cnt
            if maxprod < mprod:
                maxprod = mprod
    return count, maxprod

def count_find_num(primesL, limit):
    sol = []
    count = 0
    maxprod = 0
    baseprod = numpy.prod(primesL)
    processedNum = []
    if baseprod <= limit:
        count = count + 1
        maxprod = baseprod
        processedNum.append(baseprod)
        count,maxprod = multiplyfactors(baseprod, primesL, limit, count, maxprod,processedNum)

    if count > 0:
        sol.append(count)
        sol.append(maxprod)
    return sol


if __name__ == '__main__':
    # primesL = [163, 199, 479]
    # limit = 193399463787878
    # print(count_find_num_1(primesL, limit))

    primesL = [2, 3]
    limit = 200
    print(count_find_num(primesL, limit))
