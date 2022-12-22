# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.


def twoSum(numbers: list[int], target: int) -> list[int]:
    start = 0
    flist = []
    l = len(numbers)
    while start < l and numbers[start] <= target:
        next = start + 1
        while next < l and numbers[next] <= (target - numbers[start]):
            if numbers[start] + numbers[next] == target:
                flist.append(start + 1)
                flist.append(next + 1)
                break
            next = next + 1
        start = start + 1

    return flist


# does not work for testcases like numbers = [0,0,3,4] and target = 0
def twoSumSet(numbers: list[int], target: int) -> list[int]:
    numset = list(set(numbers))
    numset.sort()
    start = 0
    sl = len(numset)
    flist = []
    while start < sl and abs(numset[start]) <= target:
        if numset[start] + numset[start] == target:
            if numbers.count(numset[start]) >= 2:
                index1 = numbers.index(numset[start])
                index2 = index1 + 1
                flist.append(index1 + 1)
                flist.append(index2 + 1)
                break

        next = start + 1
        while next < sl and abs(numset[start] + numset[next]) <= target:
            if numset[start] + numset[next] == target:
                index1 = numbers.index(numset[start])
                index2 = numbers.index(numset[next])
                flist.append(index1 + 1)
                flist.append(index2 + 1)
                break
            next = next + 1
        start = start + 1
    return flist


if __name__ == '__main__':
    numbers = [-1, -1, 1, 1, 1]
    target = -2
    print(twoSumSet(numbers, target))

