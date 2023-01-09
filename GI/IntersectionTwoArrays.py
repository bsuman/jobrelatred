# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    finallist = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            found = nums2.index(nums1[i])
            if found > -1:
                nums2.pop(found)
                finallist.append(nums1[i])

    return finallist


if __name__ == '__main__':
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect([3, 1, 2], [1, 1]))
