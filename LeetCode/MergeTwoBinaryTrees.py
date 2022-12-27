# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order(self):
        queue = [self]
        val_list = []
        while len(queue) > 0:
            root = queue.pop(0)
            if root is not None:
                val_list.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
        return val_list


def mergeTrees(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root3 = TreeNode(root1.val + root2.val)
    root3.left = mergeTrees(root1.left,root2.left)
    root3.right = mergeTrees(root1.right, root2.right)
    return root3

if __name__ == '__main__':
    tree1_val = [1, 3, 2, 5]
    root1 = createTreeFromArray(tree1_val)
    print(root1.level_order())
    tree2_val = [2, 1, 3, 'null', 4, 'null', 7]
    root2 = createTreeFromArray(tree2_val)
    print(root2.level_order())
    root3 = mergeTrees(root1, root2)
    print(root3.level_order())
    print("===================================")


# class Solution:
#     def createTreeFromArray(self, new_node_val):
#         new_root = TreeNode(new_node_val[0])
#         queue = [new_root]
#         index = 0
#         while len(queue) > 0:
#             root3 = queue.pop(0)
#             if (2 * index + 1) < len(new_node_val):
#                 val = new_node_val[2 * index + 1]
#                 root3.left = TreeNode(val)
#                 queue.append(root3.left)
#             if (2 * index + 2) < len(new_node_val):
#                 val = new_node_val[2 * index + 2]
#                 root3.right = TreeNode(val)
#                 queue.append(root3.right)
#
#             index = index + 1
#         return new_root
#
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root1 is None and root2 is None:
#             return None
#         elif root1 is None:
#             return root2
#         elif root2 is None:
#             return root1
#
#         qu_tree1 = [root1]
#         qu_tree2 = [root2]
#         new_node_val = []
#         while len(qu_tree1) > 0 and len(qu_tree2) > 0:
#             node1 = qu_tree1.pop(0)
#             node2 = qu_tree2.pop(0)
#             if node1 is not None and node1.val != 'null' and node2 is not None and node2.val != 'null':
#                 new_node_val.append(node1.val + node2.val)
#             elif node2 is not None and node2.val != 'null':
#                 new_node_val.append(node2.val)
#             elif node1 is not None and node1.val != 'null':
#                 new_node_val.append(node1.val)
#             elif (node1 is None and node2 is not None and node2.val == 'null') or (
#                     node2 is None and node1 is not None and node1.val == 'null'):
#                 new_node_val.append('null')
#
#             if node1 is not None:
#                 qu_tree1.append(node1.left)
#                 qu_tree1.append(node1.right)
#
#             if node2 is not None:
#                 qu_tree2.append(node2.left)
#                 qu_tree2.append(node2.right)
#
#         while len(qu_tree1) > 0:
#             node1 = qu_tree1.pop(0)
#             if node1 is not None and node1.val != 'null':
#                 new_node_val.append(node1.val)
#                 qu_tree1.append(node1.left)
#                 qu_tree1.append(node1.right)
#
#         while len(qu_tree2) > 0:
#             node2 = qu_tree2.pop(0)
#             if node2 is not None and node2.val != 'null':
#                 new_node_val.append(node2.val)
#                 qu_tree1.append(node2.left)
#                 qu_tree1.append(node2.right)
#
#         new_root = self.createTreeFromArray(new_node_val)
#         return new_root
