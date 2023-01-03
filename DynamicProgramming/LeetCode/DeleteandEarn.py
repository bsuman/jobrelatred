# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

def deleteAndEarn(nums) -> int:
    if not nums:
        return 0

    freq = [0] * (max(nums) + 1)
    for n in nums:
        freq[n] += n

    dp = [0] * len(freq)
    dp[1] = freq[1]
    for i in range(2, len(freq)):
        dp[i] = max(freq[i] + dp[i - 2], dp[i - 1])

    return dp[len(freq) - 1]


if __name__ == '__main__':
    nums = [3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10]
    print(deleteAndEarn(nums))
