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

    def insert(self,ival):
        if self.val == 0 and self.right is None and self.left is None:
            self.val = ival
            return
        if self.val == ival:
            return
        else:
            if self.val < ival:
                start = self.right
                while start is not None:
                    if start.val < ival:


class Solution:

    def balancedTree(self, node):
        pass

    def sortedArrayToBST(self, nums: list[int]) -> [TreeNode]:
        node = TreeNode()
        for i in nums:
            node.insert(i)



        return []


    def __init__(self):
        pass


if __name__ == '__main__':
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    li = sol.sortedArrayToBST(nums) #[0,-3,9,-10,null,5]
    print(li)
