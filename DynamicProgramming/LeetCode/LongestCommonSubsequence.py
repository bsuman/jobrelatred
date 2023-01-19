# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text1) == 0 or len(text2) == 0:
        return 0
    elif len(text1) > len(text2):
        text1, text2 = text2, text1

    dp = [[0 for j in range(len(text2))] for i in range(len(text1))]

    for i in range(len(text1)):
        for j in range(0, len(text2)):
            if text1[i] == text2[j]:
                if i > 0 and j > 0:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1
            else:
                if i> 0:
                    top = dp[i - 1][j]
                else:
                    top = 0

                if j > 0:
                    left = dp[i][j - 1]
                else:
                    left = 0
                dp[i][j] = max(top, left)

    return dp[len(text1) - 1][len(text2) - 1]


if __name__ == '__main__':
    print(longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))
