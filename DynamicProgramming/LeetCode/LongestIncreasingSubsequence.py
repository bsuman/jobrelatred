# Given an integer array nums, return the length of the longest strictly increasing subsequence.
def lengthOfLIS(nums: list[int]) -> int:
    nl = len(nums)
    dp = [1 for i in range(nl)]
    for i in range(nl - 2, -1, -1):
        for j in range(i + 1, nl):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


if __name__ == '__main__':
    nums = [4,10,4,3,8,9]
    print(lengthOfLIS(nums))
