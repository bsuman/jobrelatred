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

    # insertion takes places from left to right starting at the root
    def insert(self, val):
        # check if the root node does not have a value
        if self.data is None:
            self.data = val  # if the root node has None as the value then update the value
            return

        qlist = [self]  # use the list to store the nodes to be traversed.
        # The list behaves as a queue i.e. FiFo ( insert at the end --> append and removal at the start --> pop(0)
        # as the nodes will be added from left to right on the available slot
        while len(qlist) > 0:
            temp = qlist.pop(0)  # first out
            if temp.left is None:
                temp.left = tnode(val)  # left node is available
                break  # and done!
            else:
                qlist.append(temp.left)  # left node occupied so queue to the list

            if temp.right is None:
                temp.right = tnode(val)  # right node is available, insert the value
                break  # and done!
            else:
                qlist.append(temp.right)  # right node occupied so queue to the list

    def search(self, val):
        # find the node with the value to be deleted
        ql = [self]
        tmp = None

        while len(ql):
            tmp = ql.pop(0)
            if tmp.data == val:
                return tmp

            if tmp.left:
                ql.append(tmp.left)

            if tmp.right:
                ql.append(tmp.right)

        return None

    # delete a node from it by making sure that the tree shrinks from the bottom (i.e. the deleted node is replaced by the bottom-most and rightmost node)
    def remove(self, val):
        # find the node with the value to be deleted and the bottom-most and right-most node to delete
        # Swap the values
        # delete the bottom-most and right-most node

        # find the bottom-most and right-most node to delete
        rightmost_node = self
        while rightmost_node.right is not None and rightmost_node.right.right is not None:
            rightmost_node = rightmost_node.right

        # find the node with the value to be deleted
        ql = [self]
        tmp = None
        while len(ql):
            tmp = ql.pop(0)
            if tmp.data == val:
                break

            if tmp.left:
                ql.append(tmp.left)

            if tmp.right:
                ql.append(tmp.right)

        if tmp is None:
            return "Value not found!"
        elif type(tmp) is tnode:
            if tmp == self:
                self = None
                return
            else:
                tmp.data = rightmost_node.right.data

        if rightmost_node.right.left is not None:
            rightmost_node.right.data = rightmost_node.right.left.data
            rightmost_node.right = None
        else:
            rightmost_node.right = None

    def inorder_traversal(self):
        if self.left is None and self.right is None:
            return [self.data]
        elif self.left is None:
            return [self.data] + self.right.inorder_traversal()
        elif self.right is None:
            return self.left.inorder_traversal() + [self.data]
        else:
            return self.left.inorder_traversal() + [self.data] + self.right.inorder_traversal()

    def preorder_traversal(self):
        if self.left is None and self.right is None:
            return [self.data]
        elif self.left is None:
            return [self.data] + self.right.preorder_traversal()
        elif self.right is None:
            return [self.data] + self.left.preorder_traversal()
        else:
            return [self.data] + self.left.preorder_traversal() + self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left is None and self.right is None:
            return [self.data]
        elif self.left is None:
            return self.right.postorder_traversal() + [self.data]
        elif self.right is None:
            return self.left.postorder_traversal() + [self.data]
        else:
            return self.left.postorder_traversal() + self.right.postorder_traversal() + [self.data]

    def levelorder_traversal(self):
        pass

    # Finding the height of the tree
    def getheight(self):
        if self.right is None or self.left is None:
            return 0
        return 1 + max(self.right.getheight(), self.left.getheight())

    def getlevel(self, val):
        level = 1
        ql = [self]
        while len(ql):
            size = len(ql)
            for numnodes in range(size):
                tmp = ql.pop(0)
                if tmp.data == val:
                    return level

                if tmp.left is not None:
                    ql.append(tmp.left)
                if tmp.right is not None:
                    ql.append(tmp.right)

            level = level + 1

    def gettotalnodes(self):
        if self.right is None and self.left is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.gettotalnodes()
        elif self.right is None and self.left is not None:
            return self.left.gettotalnodes() + 1
        else:
            return self.left.gettotalnodes() + 1 + self.right.gettotalnodes()


if __name__ == '__main__':
    root = tnode(0)
    for i in range(1, 11):
        root.insert(i)

    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())
    print(root.getheight())
    print(root.getlevel(7))
    print(root.gettotalnodes())