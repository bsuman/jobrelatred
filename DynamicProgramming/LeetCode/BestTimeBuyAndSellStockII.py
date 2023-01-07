# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

def maxProfit(prices: list[int]) -> int:
    max_prof = 0
    ln = len(prices)
    minprice = prices[0]
    for i in range(ln):
        minprice = min(minprice, prices[i])
        profit = prices[i]-minprice
        if profit > 0:
            max_prof = max_prof + profit
            minprice = prices[i]
    return max_prof


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7,6,4,3,1]))
    print(maxProfit([1,2,3,4,5]))
