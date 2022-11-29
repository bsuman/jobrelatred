# write a function CanSum(sumTarget,[list of numbers]) which takes the target sum as the input along with list of numbers
# CanSum returns true if there exists a combination of numbers whose sum is equal to the sumTarget, false otherwise
# Constraints: 1. each number occurrence in the list is unlimited 2. input the list is always including positive integers
# Use tabulation for optimization

def canSum(sumTarget, l):
    targetl = [False for i in range(sumTarget + 1)]
    targetl[0] = True
    length = len(targetl)
    for j in range(0, length):
        if targetl[j]:
            for i in l:
                if j + i < length:
                    targetl[j + i] = True

    return targetl[sumTarget]


if __name__ == '__main__':
    print(canSum(7, [5, 3, 4]))
    print(canSum(7, [4, 2]))
