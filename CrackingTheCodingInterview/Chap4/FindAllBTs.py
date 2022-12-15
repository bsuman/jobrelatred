# Find all possible binary trees with given Inorder Traversal
# Given an array that represents Inorder Traversal, find all possible Binary Trees with the given Inorder traversal and print their preorder traversals.
# Input:   in[] = {3, 2};
# Output:  Preorder traversals of different possible Binary Trees are:
#          3 2
#          2 3
# Below are different possible binary trees
#     3        2
#      \      /
#       2    3
#
# Input:   in[] = {4, 5, 7};
# Output:  Preorder traversals of different possible Binary Trees are:
#           4 5 7
#           4 7 5
#           5 4 7
#           7 4 5
#           7 5 4
# Below are different possible binary trees
#   4         4           5         7       7
#    \          \       /   \      /       /
#     5          7     4     7    4       5
#      \        /                  \     /
#       7      5                    5   4

class node:
    def __init__(self, idata):
        self.data = idata
        self.left = None
        self.right = None



def preorder_recursive(inode):
    if inode is None:
        return []

    return [inode.data] + preorder_recursive(inode.left) + preorder_recursive(inode.right)


def createBTs(inorder, start, end):
    listofBts = []
    if start > end:
        listofBts.append(None)
        return listofBts

    for i in range(start, end+1):
        ltrees = createBTs(inorder, start, i-1)
        rtrees = createBTs(inorder, i+1, end)
        for j in ltrees:
            for k in rtrees:
                n = node(inorder[i])
                n.left = j
                n.right = k
                listofBts.append(n)

    return listofBts


if __name__ == '__main__':
    inorder = [4,5,7]
    listofBts = createBTs(inorder, 0, len(inorder)-1)
    for i in listofBts:
        print(preorder_recursive(i))
