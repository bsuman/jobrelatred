# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence
# with two non-equal elements are trivially wiggle sequences.
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
# The first is not because its first two differences are positive, and the second is not because its last difference is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.
# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

def wiggleMaxLength(nums: list[int]) -> int:
    nl = len(nums)
    if nl < 2:
        return nl
    dp_inc = [1 for i in range(nl)]
    dp_dec = [1 for i in range(nl)]
    mlen = 1
    for i in range(1, nl):
        for j in range(0, i + 1):
            if nums[i] < nums[j]:
                dp_inc[i] = max(dp_inc[i], 1 + dp_dec[j])
            elif nums[i] > nums[j]:
                dp_dec[i] = max(dp_dec[i], 1 + dp_inc[j])
        mlen = max(mlen, max(dp_inc[i], dp_dec[i]))

    return mlen


if __name__ == '__main__':
    nums = [1, 7, 4, 1, 2, 5]
    print(wiggleMaxLength(nums))