# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices: list[int]) -> int:
    max_prof = 0
    ln = len(prices)
    minprice = prices[0]
    for i in range(ln):
        minprice = min(minprice, prices[i])
        max_prof = max(max_prof, prices[i]-minprice)
    return max_prof


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7,6,4,3,1]))
