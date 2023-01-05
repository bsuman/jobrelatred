# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array.
# Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once.
# Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
import math as m


def maxSubarraySumCircular(nums: list[int]) -> int:
    nl = len(nums)
    dp = [-m.inf] * nl
    dp[0] = nums[0]
    min_sum = dp[0]
    for i in range(1, nl):
        dp[i] = min(dp[i - 1] + nums[i], nums[i])
        min_sum = min(min_sum, dp[i])

    dp = [-m.inf] * nl
    dp[0] = nums[0]
    max_sum = dp[0]
    for i in range(1, nl):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(dp[i], max_sum)

    circular_sum = sum(nums) - min_sum
    if circular_sum == 0:
        return max_sum
    else:
        return max(circular_sum, max_sum)


if __name__ == '__main__':
    print(maxSubarraySumCircular([3, 1, 3, 2, 6]))
    print(maxSubarraySumCircular([5, -3, 5]))
    print(maxSubarraySumCircular([-3, -2, -3]))
    print(maxSubarraySumCircular([1, -2, 3, -2]))
