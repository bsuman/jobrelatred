# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def moveZeroes(nums: list[int]) -> None:
    numzeros = nums.count(0)
    for i in range(numzeros):
        nums.remove(0)
        nums.append(0)




if __name__ == '__main__':
    nums = [0,0,1]
    moveZeroes(nums)
    print(nums)