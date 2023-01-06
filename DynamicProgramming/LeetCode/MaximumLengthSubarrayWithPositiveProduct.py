# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
# Return the maximum length of a subarray with positive product.

import math as m


def getMaxLen(nums: list[int]) -> int:
    ln = len(nums)
    # check if the array has 0s
    result = []
    if 0 in nums:
        temp_list = []
        for i in nums:
            if i == 0:
                if len(temp_list) > 0:
                    result.append(temp_list)
                    temp_list = []
            else:
                temp_list.append(i)
        result.append(temp_list)
    else:
        result = [nums]

    max_len = 0
    for numlist in result:
        tmplen = 0
        if m.prod(numlist) > 0:
            tmplen = len(numlist)
        else:
            firstnegindex = None
            lastnegindex = None
            nl = len(numlist)
            for i in range(nl):
                num1 = numlist[i]
                num2 = numlist[-(i+1)]
                if num1 < 0 and firstnegindex is None:
                    firstnegindex = i
                if  num2 < 0 and lastnegindex is None:
                    lastnegindex = (nl-1)-i
                if firstnegindex is not None and lastnegindex is not None:
                    break

            tmplen = max(nl - (firstnegindex + 1), lastnegindex)
        if max_len < tmplen:
            max_len = tmplen
    return max_len


if __name__ == '__main__':
    print(getMaxLen([-1, -2, -3, 0, 1]))
    print(getMaxLen([0, 1, -2, -3, -4]))
    print(getMaxLen([1, -2, -3, 4]))
