# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
# is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums):
    ln = len(nums)
    if ln < 3:
        return max(nums)

    max_amount = [0] * ln
    max_amount[0] = nums[0];
    max_amount[1] = nums[1];
    max_amount[2] = nums[2] + nums[0];
    for i in range(3, ln):
        max_amount[i] = max(max_amount[i - 2], max_amount[i - 3]) + nums[i];
    return max(max_amount[ln - 1], max_amount[ln - 2]);


if __name__ == '__main__':
    nums = [82,217,170,215,153,55,185,55,185,232,69,131,130,102]
    print(rob(nums))
