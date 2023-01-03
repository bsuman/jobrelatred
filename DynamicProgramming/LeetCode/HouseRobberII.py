# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums: list[int]) -> int:
    ln = len(nums)
    if ln < 4:
        return max(nums)
    amount1 = robhouse(nums[:len(nums)-1])
    amount2 = robhouse(nums[len(nums):0:-1])
    return max(amount1, amount2)


def robhouse(nums: list[int]) -> int:
    ln = len(nums)
    max_amount = [0] * ln
    max_amount[0] = nums[0];
    max_amount[1] = nums[1];
    max_amount[2] = nums[2] + nums[0];
    for i in range(3, ln):
        max_amount[i] = max(max_amount[i - 2], max_amount[i - 3]) + nums[i];
    return max(max_amount[ln - 1], max_amount[ln - 2]);


if __name__ == '__main__':
    nums = [2, 3, 2]
    print(rob(nums))
    nums = [1, 2, 3, 1]
    print(rob(nums))
    nums = [5, 4, 6, 8,9,10,12]
    print(rob(nums))