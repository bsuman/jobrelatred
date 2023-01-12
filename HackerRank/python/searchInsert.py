def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums)
    while (high - low) >= 0:
        # calculates the middle index
        mid = (high + low) // 2
        if nums[mid] == target:  # check if the target is the middle element
            return mid  # found, return index
        # check if target is bigger than the previous element from middle but smaller than the middle then return mid-1 as the position to insert
        elif nums[mid] > target:
            if mid == 0:
                return 0
            elif mid - 1 > 0 and nums[mid - 1] < target:
                return mid
            else:
                high = mid - 1
        elif nums[mid] < target:
            if mid + 1 == len(nums):
                return len(nums)
            elif mid + 1 < len(nums) and nums[mid + 1] > target:
                return mid + 1
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    nums = [1,3]
    print(searchInsert(nums, 0))
