# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.


def numberOfArithmeticSlices(nums) -> int:
    ln = len(nums)
    # array for maintaining the number of arithmetic subarrays possible at the index
    dp_num = [0] * ln
    # as minimum size of the arithmetic subarrays should be 3,
    # no subarrays are possible with just last and second last elements of num
    dp_num[ln - 1] = 0
    dp_num[ln - 2] = 0
    previous_diff = nums[ln - 1] - nums[ln - 2]
    start = ln - 3
    for i in range(start, -1,-1):
        curr_diff = nums[i + 1] - nums[i]
        if curr_diff == previous_diff:
            dp_num[i] = dp_num[i + 1] + 1
        else:
            dp_num[i] = 0
            dp_num[i-1] = 0
            start = i-3
            previous_diff = curr_diff
    max_num = sum(dp_num)
    return max_num


if __name__ == '__main__':
    nums = [1, 2, 3, 4,8,7,6,5,4]
    print(numberOfArithmeticSlices(nums))
    nums = [1, 2, 3, 4]
    print(numberOfArithmeticSlices(nums))
