# write a function CanSum(sumTarget,[list of numbers]) which takes the target sum as the input along with list of numbers
# CanSum returns true if there exists a combination of numbers whose sum is equal to the sumTarget, false otherwise
# Constraints: 1. each number occurrence in the list is unlimited 2. input the list is always including positive integers

def CanSum(sumTarget, l,d ={}):
    if sumTarget == 0:
        return True
    elif sumTarget in d.keys():
        return d[sumTarget]
    else:
        for i in l:
            remainder = sumTarget - i
            if remainder >= 0:
                isSumPossible = CanSum(remainder, l,d)
                d[sumTarget] = isSumPossible
                if isSumPossible:
                    return isSumPossible
        return False

if __name__ == '__main__':
    d= {}
    print(CanSum(7, [5, 3, 4, 7],d))
    d = {}
    print(CanSum(7, [4, 2],d))
    d = {}
    print(CanSum(8, [2,3,5],d))
    d = {}
    print(CanSum(300, [7, 14],d))