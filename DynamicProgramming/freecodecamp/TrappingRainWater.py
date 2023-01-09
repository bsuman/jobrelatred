# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


def trap(height):
    hl = len(height)
    left_max_dp = [-1] * hl
    right_max_dp = [-1] * hl
    left_max_dp[0] = height[0]
    right_max_dp[hl - 1] = height[hl - 1]
    for i in range(1, hl):
        left_max_dp[i] = max(height[i], left_max_dp[i - 1])
        right_max_dp[-i - 1] = max(height[-i - 1], right_max_dp[-i])

    rainwater = 0
    for i in range(0, hl):
        rainwater = rainwater + min(left_max_dp[i], right_max_dp[i]) - height[i]
    return rainwater


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))
