# Best Time to Buy and Sell Stock with Cooldown
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


def maxProfit(prices: list[int]) -> int:
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

        # at every given day, a cooldown is possible i.e. to do nothing
        cooldown = getprofit(i + 1, state)
        # if we are in a buying state
        if state:
            # then on the next day (increment the day by 1) we can not buy so change state to not buying
            # profit made that day after the buying transaction, is the reduced by the cost of the bought share
            buy = getprofit(i + 1, not state) - prices[i]
            # choose the max of profit made either by buying the share or by cool down
            state_info[(i, state)] = max(buy, cooldown)
        else:
            # if we have bought the share on an earlier date, then we can either sell or cooldown
            # if we sell, then we cannot do anything on the next day, so we increment the day by 2 and
            # after the gap of a day we can buy again so change the state to not of selling
            # profit made by the transaction is incremented by the selling price
            sell = getprofit(i + 2, not state) + prices[i]
            # choose the max of profit made either by selling the share or by cool down
            state_info[(i, state)] = max(sell, cooldown)
        return state_info[(i, state)]

    return getprofit(0, 1)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(maxProfit([1, 2, 3, 0, 2]))
