# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if root is None:
            return

        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.right is not None and node.left is not None:
                node.left.next = node.right
            if node.right is not None and node.next is not None:
                node.right.next = node.next.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root
