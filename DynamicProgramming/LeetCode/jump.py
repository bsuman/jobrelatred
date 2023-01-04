# Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

def jump(nums: list[int]) -> int:
    ln = len(nums)
    dp = [None] * ln
    dp[0] = 0
    for i in range(0, ln - 1):
        num_steps = nums[i]
        for j in range(i + 1, i + num_steps + 1):
            if j < ln:
                if dp[j] is None:
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[i] + 1, dp[j])
    return dp[ln-1]


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
    nums = [2, 0, 2]
    print(jump(nums))
    nums = [2, 3, 0, 1, 4]
    print(jump(nums))
