# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
import math


def coinChange(coins: list[int], amount: int) -> int:
    targetl = [None for i in range(amount + 1)]
    targetl[0] = []
    length = len(targetl)

    for i in range(length):
        if targetl[i] is not None:
            for j in range(len(coins)):
                if i + coins[j] < length:
                    new = [coins[j]] + targetl[i]
                    if targetl[i + coins[j]] is None or len(targetl[i + coins[j]]) > len(new):
                        targetl[i + coins[j]] = new

    if targetl[amount] is None:
        return -1
    else:
        return len(targetl[amount])


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins,amount))