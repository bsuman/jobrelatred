# Given an array of distinct integers nums and a target integer target,
# return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.

def combinationSum4(nums: list[int], target: int) -> int:
    dp = [0 for i in range(target + 1)]
    dp[0] = 1

    for comb_sum in range(target + 1):

        for num in nums:
            if comb_sum - num >= 0:
                dp[comb_sum] += dp[comb_sum - num]
    return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))
