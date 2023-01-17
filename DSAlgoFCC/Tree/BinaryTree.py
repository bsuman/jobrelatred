# Implement a binary tree using Python, and show its usage with some examples.
# we require the binary tree to have some additional properties:

# Keys and Values: Each node of the tree stores a key (a username) and a value (a User object).
# Only keys are shown in the picture above for brevity.
# A binary tree where nodes have both a key and a value is often referred to as a map or treemap (because it maps keys to values).

# Binary Search Tree: The left subtree of any node only contains nodes with keys that are lexicographically smaller than the node's key,
# and the right subtree of any node only contains nodes with keys that lexicographically larger than the node's key.
# A tree that satisfies this property is called a binary search trees, and it's easy to locate a specific key by traversing a single path down from the root note.
#
#
# Balanced Tree: The tree is balanced i.e. it does not skew too heavily to one side or the other.
# The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level.

import UserDatabase as userdb


class BSTree:
    def __init__(self, iuser=None):
        self.user = iuser
        if self.user is not None:
            self.left = BSTree()
            self.right = BSTree()
        else:
            self.left = None
            self.right = None

    def isEmpty(self):
        return self.user is None

    def find_user(self, nuser):
        while self.user is not None and nuser is not None:
            if nuser.username == self.user.username:
                return True
            elif nuser.username < self.user.username:
                return self.left.find_user(nuser)
            else:
                return self.right.find_user(nuser)
        return False

    def minValue(self):
        if self.left is None:
            return self.user
        else:
            return self.left.minValue()

    def maxValue(self):
        if self.right is None:
            return self.user
        else:
            return self.right.maxValue()

    def insert_user(self, nuser):
        if self.user is None:
            self.user = nuser
            self.left = BSTree()
            self.right = BSTree()
            return

        if self.find_user(nuser):
            print("The user with username = {} already exists in the database!".format(nuser.username))
        else:
            if self.user.username < nuser.username:
                self.right.insert_user(nuser)
            else:
                self.left.insert_user(nuser)

    def inorder_Traversal(self): #LNR
        if self.isEmpty():
            return []
        else:
            return self.left.inorder_Traversal() + [self.user.username] + self.right.inorder_Traversal()

    def preorder_Traversal(self): #NLR
        if self.isEmpty():
            return []
        else:
            return [self.user.username] + self.left.inorder_Traversal() + self.right.inorder_Traversal()

    def postorder_Traversal(self): #LRN
        if self.isEmpty():
            return []
        else:
            return  self.left.inorder_Traversal() + self.right.inorder_Traversal() + [self.user.username]

    def __str__(self):
        return str(self.inorder_Traversal())

    def delete_user(self, duser):
        if self.user is None:
            return
        else:
            if self.user.username < duser.username:
                self.right.delete_user(duser)
                return

            if self.user.username > duser.username:
                self.left.delete_user(duser)
                return

            if self.user.username == duser.username:
                if self.left is None and self.right is None:
                    self.user = None
                elif self.left is None and self.right is not None:
                    self.user = self.right.user
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.user = self.left.maxValue()
                    self.left.delete_user(self.left.maxValue())
                return


if __name__ == '__main__':
    t = BSTree()
    users = []
    user1 = userdb.User("bSuman","suman bidarahalli", "suman.darmstadt@gmail.com")
    user2 = userdb.User("dontbSuman", "suman Bidarahalli", "suman1.darmstadt@gmail.com")
    user3 = userdb.User("maybSuman", "Suman bidarahalli", "suman2.darmstadt@gmail.com")
    user4 = userdb.User("aSuman", "Suman Bidarahalli", "suman3.darmstadt@gmail.com")
    user5 = userdb.User("caneffectiveSuman", "Suman_Bidarahalli", "suman4.darmstadt@gmail.com")
    users.append(user1)
    users.append(user2)
    users.append(user3)
    users.append(user4)
    users.append(user5)

    for i in users:
        t.insert_user(i)

    print(t)

    t.delete_user(user3)
    print(t)

    t.insert_user(user3)
    print(t)

    t.delete_user(user5)
    print(t)

    t.insert_user(user5)
    print(t)

    t.delete_user(user4)
    print(t)
