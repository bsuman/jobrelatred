# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
import math as m


# works only for positive integer array or array of integers with even number of negative integer
def maxProduct_old(nums: list[int]) -> int:
    ln = len(nums)
    product_list = [-m.inf] * ln
    product_list[0] = nums[0]
    max_prod = nums[0]
    for i in range(1, ln):
        product_list[i] = max(product_list[i - 1] * nums[i], nums[i])
        if max_prod < product_list[i]:
            max_prod = product_list[i]
    all_prod = m.prod(nums)
    if max_prod < all_prod:
        max_prod = all_prod
    return max_prod


def maxProduct(nums: list[int]) -> int:
    ln = len(nums)
    result = nums[0]
    product_1 = nums[0]
    product_2 = nums[0]
    for i in range(1, ln):
        tmp = max(nums[i], product_1 * nums[i], product_2 * nums[i])
        product_2 = min(nums[i], product_1 * nums[i], product_2 * nums[i])
        product_1 = tmp
        result = max(result, product_1)

    return result


if __name__ == '__main__':
    print(maxProduct([2, -5, -2, -4, 3]))
    print(maxProduct([2, 3, -2, 4]))
    print(maxProduct([-2, 0, -1]))
