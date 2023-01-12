# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
import heapq as hpq


def sortedSquares(nums):
    squares = []
    for i in nums:
        squares.insert(i * i)
    squares.sort()
    return squares


def sortedSquaresHeap(nums):
    squares = []
    for i in nums:
        squares.append(i * i)
    hpq.heapify(squares)
    return squares


def sortedSquaresbin(nums: list[int]) -> list[int]:
    low = 0
    high = len(nums) - 1
    numtimes = len(nums)
    squares = []
    while numtimes > 0:
        right = nums[high]
        left = nums[low]
        if abs(right) > abs(left):
            squares.insert(0,pow(right, 2))
            high = high - 1
        elif abs(right) <= abs(left):
            squares.insert(0, pow(left, 2))
            low = low + 1

        numtimes = numtimes - 1

    return squares


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquaresbin(nums))