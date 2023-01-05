# Given an integer array nums, find the subarray with the largest sum, and return its sum.
import math as m


def maxSubArray(nums: list[int]) -> int:
    nl = len(nums)
    dp = [-m.inf] * nl
    dp[0] = nums[0]
    max_sum = dp[0]
    for i in range(1, nl):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        if dp[i] > max_sum:
            max_sum = dp[i]

    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray([1]))
    print(maxSubArray([5, 4, -1, 7, 8]))
