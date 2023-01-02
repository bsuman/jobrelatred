# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# importing functools for reduce()
import functools


def singleNumber(nums):
    return functools.reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    print(singleNumber([2, 2, 1]))
