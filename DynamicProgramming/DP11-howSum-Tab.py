# write a function howSum(targetSum,l) that takes in a targetSum and a list of numbers as arguments
# function returns a list of combination of elements whose sum is equal to targetSum
# if no combination exists then return null
# incase of multiple combinations possible return any valid combinations
# Use tabulation for optimization

def howSum(targetSum, l):
    targetl = [None for i in range(targetSum + 1)]
    targetl[0] = []
    length = len(targetl)

    for i in range(length):
        if targetl[i] is not None:
            for j in range(len(l)):
                if i + l[j] < length:
                    targetl[i + l[j]] = targetl[i] + [l[j]]
                    if targetl[targetSum] is not None:
                        return targetl[targetSum]

    return None


if __name__ == '__main__':
    sol = howSum(7, [5, 3, 4])
    print(sol)
    sol = howSum(8, [2, 3, 5])
    print(sol)
    sol = howSum(8, [3, 3, 2])
    print(sol)
    sol = howSum(8, [4, 3, 2])
    print(sol)
    sol = howSum(7, [4, 2])
    print(sol)
