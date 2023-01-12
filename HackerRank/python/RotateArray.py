# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# possibility 1
def rotatepos1(nums: list[int], k: int) -> None:
    ls = len(nums)
    swaplist = nums
    for i in range(ls):
        index = i + k
        if index < ls:
            nums[index] = swaplist[i]
        else:
            index = index % ls
            nums[index] = swaplist[i]

    print(swaplist)


# possibility 2: mirror technique
def rotatepos2(nums: list[int], k: int) -> None:
    nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]

if __name__ == '__main__':
    n = [-1,-100,3,99]
    k =2
    rotatepos2(n, k)
    print(n)
    n =[1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotatepos2(n, k)
    print(n)