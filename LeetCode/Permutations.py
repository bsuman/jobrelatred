# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

def permute(nums):
    flist = []
    ln = len(nums)
    queue = []
    for i in nums:
        queue.append([i])

    while len(queue) > 0:
        numlist = queue.pop(0)
        if len(numlist) == ln:
            flist.append(numlist)
        else:
            for num in nums:
                if num not in numlist:
                    tmp = [num] + numlist
                    queue.append(tmp)

    return flist

if __name__ == '__main__':
    nums= [1,2,3]
    print(permute(nums))
    nums = [0, 1]
    print(permute(nums))
    nums = [1]
    print(permute(nums))