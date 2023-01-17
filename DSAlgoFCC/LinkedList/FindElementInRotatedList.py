# Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.
#
# Note: Find the element in O(logN) time and assume that all the elements are distinct.
#
# Example:
#
# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
# Output : Found at index 8
#
#
# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
# Output : Not found
#
# Input : arr[] = {30, 40, 50, 10, 20}, key = 10
# Output : Found at index 3

def binarySearchRotatedList(a, low, high):
    if high - low <= 0:  # list is empty
        return
    mid = (high + low) // 2
    if a[mid - 1] < a[mid]:
        return mid
    else:
        if a[mid] > a[high]:
            return binarySearchRotatedList(a, mid + 1, high)
        elif a[mid] < a[high]:
            return binarySearchRotatedList(a, low, mid)


def binarySearch(a, low, high, key):
    if high - low < 0:  # list is empty
        return -1

    mid = (high + low) // 2
    if a[mid] == key:
        return mid
    elif a[mid] > key:
        return binarySearch(a, low, mid, key)
    else:
        return binarySearch(a, mid + 1, high, key)


def Search(a, key):
    low, high = 0, len(a) - 1
    numrotations = binarySearchRotatedList(a, low, high)
    if a[numrotations] < key:
        return binarySearch(a, 0, numrotations, key)
    else:
        return binarySearch(a, numrotations + 1, high,key)


if __name__ == '__main__':
    a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print("The given key = {} is found at position = {}".format(key, Search(a, key)))

    a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 30
    print("The given key = {} is found at position = {}".format(key, Search(a, key)))

    a = [30, 40, 50, 10, 20]
    key = 10
    print("The given key = {} is found at position = {}".format(key, Search(a, key)))
