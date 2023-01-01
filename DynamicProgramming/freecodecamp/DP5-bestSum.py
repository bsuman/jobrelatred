# write a function bestSum(targetSum,l) that takes in a targetSum and a list of numbers as arguments
# function returns the shortest list of combination of elements whose sum is equal to targetSum
# if no combination exists then return null
# incase of multiple shortest equal length of combinations possible return any valid combinations


def bestSum(targetSum, l, d):
    if targetSum == 0:
        return []
    elif targetSum < 0:
        return None
    elif targetSum in d.keys():
        return d[targetSum]

    shortestCombi = None
    for i in l:
        remainder = targetSum - i
        result = bestSum(remainder, l,d)
        if result is not None:
            combi = [*result, i]
            if shortestCombi is None or len(combi) < len(shortestCombi):
                shortestCombi = combi

    d[targetSum] = shortestCombi
    return shortestCombi


if __name__ == '__main__':
    d = {}
    sol = bestSum(7, [7, 4, 3], d)
    print(sol)

    d = {}
    print(bestSum(300, [7, 14],d))

    d = {}
    print(bestSum(100, [1,2,5,25],d))