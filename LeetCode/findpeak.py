
def approach(nums: list[int]):
    low = 0
    high = len(nums)-1
    while low<high:
        mid= (high+low) //2
        if nums[mid] > nums[mid+1]:
            high = mid
        elif nums[mid] < nums[mid+1]:
            low = mid+1
    return low
def findPeakElement(nums: list[int]) -> int:
    for index in range(len(nums)):
        if index - 1 >=0 and index+1<len(nums):
            if nums[index-1] < nums[index] and nums[index+1] < nums[index]:
                return index


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(approach(nums))
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(approach(nums))