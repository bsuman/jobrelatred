# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

def minCostClimbingStairsop(cost) -> int:
    n = len(cost)
    step_cost = [0] * (n + 1)
    for i in range(2, n + 1):
        onestep = step_cost[i - 1] + cost[i - 1]
        twostep = step_cost[i - 2] + cost[i - 2]
        step_cost[i] = min(onestep, twostep)
    return step_cost[n]


def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    step_cost = [None] * (n + 2)
    if n == 1:
        return cost[0]
    elif n == 2:
        return min(cost[1], cost[0])
    step_cost[0] = 0
    step_cost[1] = cost[0]
    step_cost[2] = cost[1]
    for i in range(3, n + 2):
        if i < n + 1:
            step_cost[i] = min(step_cost[i - 1], step_cost[i - 2]) + cost[i - 1]
        else:
            step_cost[i] = min(step_cost[i - 1], step_cost[i - 2])

    return step_cost[n + 1]


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))
    cost = [1, 100]
    print(minCostClimbingStairs(cost))
