# Best Time to Buy and Sell Stock with Transaction Fee
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(prices: list[int], fee: int) -> int:
    # state = 1 --> buying
    # state = 0 --> not buying
    state_info = {}

    # key : index + state
    # value: profit at given key
    def getprofit(i, state):
        # if the index is out of range then we made no profit because we made no transactions
        if i >= len(prices):
            return 0

        # if already computed for the given i and state the max profit then return
        if (i, state) in state_info.keys():
            return state_info[(i, state)]

        # at every given day, doing nothing is possible
        donothing = getprofit(i + 1, state)
        # if we are in a buying state
        if state:
            # then on the next day (increment the day by 1) we can not buy so change state to not buying
            # profit made that day after the buying transaction, is the reduced by the cost of the bought share
            buy = getprofit(i + 1, not state) - prices[i]
            # choose the max of profit made either by buying the share or by doing nothing
            state_info[(i, state)] = max(buy, donothing)
        else:
            # if we have bought the share on an earlier date, then we can either sell or do nothing
            # if we sell, then we can on the next day buy, so change the state to buying
            # profit made by the transaction is incremented by the selling price - the transaction fee
            sell = getprofit(i + 1, not state) + prices[i] - fee
            # choose the max of profit made either by selling the share or by doing nothing
            state_info[(i, state)] = max(sell, donothing)
        return state_info[(i, state)]

    return getprofit(0, 1)

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(maxProfit(prices,fee))
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    print(maxProfit(prices, fee))