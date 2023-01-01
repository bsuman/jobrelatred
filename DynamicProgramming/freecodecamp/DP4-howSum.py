# write a function howSum(targetSum,l) that takes in a targetSum and a list of numbers as arguments
# function returns a list of combination of elements whose sum is equal to targetSum
# if no combination exists then return null
# incase of multiple combinations possible return any valid combinations

def howSum(targetSum, l,d):
    if targetSum == 0:
        return []
    elif targetSum < 0:
        return None
    elif targetSum in d.keys():
        return d[targetSum]
    for i in l:
        result = howSum(targetSum - i, l, d)
        if result is not None:
            d[targetSum] = [*result, i]
            return d[targetSum]

    d[targetSum] = None
    return None

if __name__ == '__main__':
    d = {}
    sol = howSum(7, [4, 3],d)
    print(sol)

    d = {}
    sol = howSum(8, [2, 3, 5], d)
    print(sol)

    d = {}
    sol = howSum(7, [4,2],d)
    print(sol)

    d = {}
    sol = howSum(300, [7,14],d)
    print(sol)
