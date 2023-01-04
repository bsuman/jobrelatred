# You are given an integer array nums.
# You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# performance issue
def canJump_old(nums: list[int]) -> bool:
    ln = len(nums)
    step_possible = [False] * ln
    step_possible[0] = True
    for i in range(0, ln):
        if step_possible[i]:
            for j in range(nums[i] + 1):
                if i + j < ln and not step_possible[i + j]:
                    step_possible[i + j] = True
                    if step_possible[ln - 1]:
                        return step_possible[ln - 1]
    return step_possible[ln - 1]


def canJump(nums: list[int]) -> bool:
    ln = len(nums)
    target = ln - 1
    for i in range(ln - 2, -1, -1):
        if nums[i] >= target - i:
            target = i

    if target == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [2, 0, 2]
    print(canJump(nums))
    nums = [3, 2, 1, 0, 4]
    print(canJump(nums))
    nums = [1, 2]
    print(canJump(nums))
    nums = [0]
    print(canJump(nums))
    nums = [3, 2, 1, 1, 4]
    print(canJump(nums))
