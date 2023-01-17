# You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.
#
# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
#
# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
#
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

# Analysis:
# As per definition of the 'rotation', last element is removed from last position and adding it before the first element
# That means each element position is incremented by one with each rotation.
# one way of getting the number of rotations:
# assumption: as the list is a sorted list in ascending order, the unrotated list should have the smallest element in the position 0.
# find the smallest element in the rotated list and get the position in the rotated list.
# number of rotations = position of the smallest element in the rotated list - expected position of the smallest element in an unrotated list

# testcases:
# 1. input empty list [] --> num rotations --> 0
# 2. input consists of one element ---> [x] ---> 1
# 3. inputs are unique, so there is one smallest num .

def count_rotations_linear(nums):
    position = 0  # the number of rotations is initialized to 0

    while position < len(nums):  # When the scan to find the minimum element is over i.e end of the list

        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position - 1]:  # How to perform the check?
            return position

        # Move to the next position
        position += 1

    position = 0
    return position

def binarySearch(nums, left, right):
    if right -left <0:
        return 0
    mid = (left + right) // 2
    if mid -1 >=0 and nums[mid] < nums[mid -1]:
        return mid
    elif nums[mid] < nums[right]:
        return binarySearch(nums,left, mid)
    else:
        return binarySearch(nums,mid + 1, right)

def count_rotations_binary(nums):
    left = 0
    right = len(nums) - 1
    pos = binarySearch(nums, left, right)

    return pos

if __name__ == '__main__':
    l = [5, 6, 9, 0, 2, 3, 4]
    print(count_rotations_binary(l))
    l = [1]
    print(count_rotations_binary(l))
    l = []
    print(count_rotations_binary(l))
    l = [0,1,2,3,4,5]
    print(count_rotations_binary(l))
    l = [1,2,3,4,5,0]
    print(count_rotations_binary(l))
    l =[5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    print(count_rotations_binary(l))
    l = [1,1,2,2,2,3,3,4,5,5,5,0,0,0]
    print(count_rotations_binary(l))
    l = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5 ]
    print(count_rotations_binary(l))
    l = [ 0,2, 3, 3, 3, 3, 4, 4,5, 6, 6, 9, 9, 9, 0]
    print(count_rotations_binary(l))