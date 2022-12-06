# Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTree(self, nums, low, high):
        if high <= low:
            return None
        mid = (high + low) // 2
        node = TreeNode(nums[mid])
        return [node.val] + [self.binaryTree(nums,low,mid)] + [self.binaryTree(nums,mid+1,high)]

    def sortedArrayToBST(self, nums: list[int]) -> [TreeNode]:
        low = 0
        high = len(nums)
        node = self.binaryTree(nums, 0, high)
        return node


    def __init__(self):
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    li = sol.sortedArrayToBST(nums) #[0,-3,9,-10,null,5]
    print(li)
