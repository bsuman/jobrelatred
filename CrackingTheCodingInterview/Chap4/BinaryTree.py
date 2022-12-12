# implement a binary tree
# Binary Tree Representation
#
# A Binary tree is represented by a pointer to the topmost node (commonly known as the “root”) of the tree.
# If the tree is empty, then the value of the root is NULL. Each node of a Binary Tree contains the following parts:
# Data
# Pointer to left child
# Pointer to right child
#
# Basic Operation On Binary Tree:
# Inserting an element.
# Removing an element.
# Searching for an element.
# Traversing the tree.
#
# Auxiliary Operation On Binary Tree:
# Finding the height of the tree
# Find the level of a node of the tree
# Finding the size of the entire tree.


class tnode:
    def __init__(self, idata):
        self.data = idata
        self.left = None
        self.right = None

    def checkifsubtreeempty(self):
        return self.left is None or self.right is None or self.right.data is None or self.left.data is None

    def insert(self, val):
        ntnode = tnode(val)
        if self.left is None:
            self.left = ntnode
        elif self.right is None:
            self.right = ntnode
        else:
            if self.left.checkifsubtreeempty():
                self.left.insert(val)
            elif self.right.checkifsubtreeempty():
                self.right.insert(val)
            else:
                self.left.insert(val)

    def search(self, val):
        if self.data == val:
            return [self]
        elif self.left is None and self.right is not None:
            return self.right.search(val)
        elif self.right is None and self.left is not None:
            return self.left.search(val)
        elif self.right is None and self.left is None:
            return []
        else:
            return self.left.search(val) + self.right.search(val)

    def remove(self, val):
        if self.data is None:
            return
        else:
            if self.data == val:
                if self.right is None and self.left is None:
                    self.data = None
                    return
                elif self.left is None and self.right is not None:
                    tmp = self.right.data
                    return self.right.remove(self.right.data)
                    self.data = tmp
                    return
                elif self.right is None and self.left is not None:
                    tmp = self.left.data
                    return self.left.remove(self.left.data)
                    self.data = tmp
                    return
            if self.left is not None:
                self.left.remove(val)
            if self.right is not None:
                self.right.remove(val)
            return

    def inorder_traversal(self):
        if self.left is None and self.right is None:
            return [self.data]
        elif self.left is None:
            return [self.data] + self.right.inorder_traversal()
        elif self.right is None:
            return self.left.inorder_traversal() + [self.data]
        else:
            return self.left.inorder_traversal() + [self.data] + self.right.inorder_traversal()


if __name__ == "__main__":
    tree = tnode(0)
    for i in range(1, 10):
        tree.insert(i)
    print(tree.inorder_traversal())
    result = tree.search(4)
    if len(result) != 0:
        print("found element = {}".format(result[0].data))
    result = tree.search(100)
    if len(result) != 0:
        print("found element = {}".format(result[0].data))
    else:
        print("element not found")

    result = tree.search(9)
    if len(result) != 0:
        print("found element = {}".format(result[0].data))
    else:
        print("element not found")
    tree.remove(9)
    print(tree.inorder_traversal())
    tree.insert(9)
    print(tree.inorder_traversal())
