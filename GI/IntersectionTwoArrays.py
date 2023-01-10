# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# not efficient as to get the index of the element, the index function looks through all elements until the element is found
# if the searched element is the last element, then the index function can have O(n) complexity, making the whole function have O(m*n) and n2 if m=n
def intersect_1(nums1, nums2):
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

# if n size of nums1 and m size of nums2 then complexity will be O(n+m) and space complexity will be O(n)
def intersect(nums1, nums2):
    ln1 = len(nums1)
    ln2 = len(nums2)
    if ln1 > ln2:
        nums1, nums2 = nums2, nums1

    nummap = {}
    finallist = []
    for i in nums1:
        if i in nummap.keys():
            nummap[i] += 1
        else:
            nummap[i] = 1

    for j in nums2:
        if j in nummap.keys() and nummap[j] > 0:
            finallist.append(j)
            nummap[j] -= 1

    return finallist


if __name__ == '__main__':

    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect([3, 1, 2], [1, 1]))
    print(intersect([1, 2, 2, 1], [2, 2]))