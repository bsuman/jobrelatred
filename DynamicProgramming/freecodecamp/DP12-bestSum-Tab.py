# function returns the shortest list of combination of elements whose sum is equal to targetSum
# if no combination exists then return null
# incase of multiple shortest equal length of combinations possible return any valid combinations
# Use tabulation for optimization

def bestSum(targetSum, l):
    targetl = [None for i in range(targetSum + 1)]
    targetl[0] = []
    length = len(targetl)

    for i in range(length):
        if targetl[i] is not None:
            for j in range(len(l)):
                if i + l[j] < length:
                    new = [l[j]] + targetl[i]
                    if targetl[i + l[j]] is None or len(targetl[i + l[j]]) > len(new):
                        targetl[i + l[j]] = new

    return targetl[targetSum]



if __name__ == '__main__':
   print(bestSum(8, [5,3,2]))
   print(bestSum(8, [8,6, 4,2]))
   print(bestSum(100, [1, 2, 5, 25]))