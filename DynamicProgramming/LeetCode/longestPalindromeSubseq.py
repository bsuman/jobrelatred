# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

def longestPalindromeSubseq(s: str) -> int:
    ls = len(s)
    dp = [[0 for i in range(ls)] for i in range(ls)]
    for i in range(ls):
        dp[i][i] = 1

    i = 0
    distance = 1
    while i + distance < ls:
        t1 = i
        t2 = i + distance
        while t1 < ls and t2 < ls:
            if s[t1] == s[t2]:
                dp[t1][t2] = 2 + dp[t1 + 1][t2 - 1]
            else:
                dp[t1][t2] = max(dp[t1 + 1][t2], dp[t1][t2 - 1])
            t1 = t1 + 1
            t2 = t2 + 1
        distance = distance + 1
    return dp[0][ls - 1]


if __name__ == '__main__':
    print(longestPalindromeSubseq("bbbab"))
