# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

def minDistance(word1: str, word2: str) -> int:
    lw2 = len(word2)
    lw1 = len(word1)
    if lw2 == 0:
        return 0
    elif lw1 == 0:
        return lw2

    dp = [[0 for i in range(lw1+1)] for j in range(lw2+1)]
    for i in range(lw2+1):
        dp[i][0] = i

    for i in range(lw1+1):
        dp[0][i] = i

    for i in range(1,lw2+1):
        for j in range(1,lw1+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+ 1

    return dp[lw2][lw1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1,word2))