# write a function to determine if given Tree is height balanced

class node:
    def __init__(self, ival):
        self.val = ival
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        root = node(val)
    else:

        if root.val < val:
            if root.right is None:
                root.right = node(val)
            else:
                insert(root.right, val)
        else:
            if root.left is None:
                root.left = node(val)
            else:
                insert(root.left, val)


def getheight(root):
    if root is None:
        return 0
    return 1 + max(getheight(root.left), getheight(root.right))


def isheightbalanced(root):
    height = abs(getheight(root.left) - getheight(root.right))
    return height <= 1


def isBalanced(root):
    # Base condition
    if root is None:
        return 0

    # Compute height of left subtree
    lh = isBalanced(root.left)

    # If left subtree is not balanced,
    # return -1
    if lh == -1:
        return -1

    # Do same thing for the right subtree
    rh = isBalanced(root.right)
    if rh == -1:
        return -1

    # Allowed values for (lh - rh) are 1, -1, 0
    if abs(lh - rh) > 1:
        return -1
    elif max(lh, rh) == 0:
        return 0
    else:
        return max(lh, rh) + 1


if __name__ == '__main__':
    root = node(4)
    ht = isBalanced(root)
    print(ht)
    for i in [1, 2, 3, 5, 8]:
        insert(root, i)
    if isheightbalanced(root):
        print("Tree height balanced")
    else:
        print("Tree height not balanced")
