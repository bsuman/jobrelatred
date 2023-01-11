# Unique Binary Search Trees
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# number of unique BST is catalan number series
def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] = dp[i] + (dp[j - 1] * dp[i - j])

    return dp[n]


if __name__ == '__main__':
    print(numTrees(3))
