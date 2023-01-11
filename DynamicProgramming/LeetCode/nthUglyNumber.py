# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

def nthUglyNumber(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    index2, index3, index5 = 0, 0, 0
    uglynum_2 = dp[index2] * 2
    uglynum_3 = dp[index3] * 3
    uglynum_5 = dp[index5] * 5

    for i in range(1, n):
        next_uglynum = min(uglynum_2, uglynum_3, uglynum_5)
        dp[i] = next_uglynum
        if next_uglynum == uglynum_2:
            index2 = index2 + 1
            uglynum_2 = dp[index2] * 2
        if next_uglynum == uglynum_3:
            index3 = index3 + 1
            uglynum_3 = dp[index3] * 3
        if next_uglynum == uglynum_5:
            index5 = index5 + 1
            uglynum_5 = dp[index5] * 5

    return dp[n-1]


if __name__ == '__main__':
    print(nthUglyNumber(1))
    print(nthUglyNumber(10))
