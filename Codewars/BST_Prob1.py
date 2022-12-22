# Binary Search Trees
# A Tree consists of a root, which is of type Node, possibly a left subtree of type Tree, and possibly a right subtree of type Tree.
# If the left subtree is present, then all its nodes are less than the parent tree's root;
# if the right tree is present, then all its nodes are greater than the parent tree's root.
#
# In this kata, classes Tree and Node have been provided.
# However, the methods __eq__, __ne__, and __str__ are missing from the Tree class.
# Your job is to provide the implementation of these methods.
# The example test cases should provide enough information to implement these methods correctly.
#
# As an illustrative example, here is the string representation of a tree that has two nodes,
# 'B' at the root and 'C' at the root of the right subtree.
# The left subtree is missing and the right subtree is a leaf, i.e., has no subtrees:
#
# "[_ B [C]]"
# This tree is obtained by evaluating the following expression:
#
# Tree(Node('B'), None, Tree(Node('C')))
# Notice in particular that when one subtree, but not both, is missing, an underscore is in its place,
# a single space separates the root node from the subtrees, and when both subtrees are missing,
# the root node is enclosed in brackets.

class Node(object):

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


class Tree(object):

    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def __str__(self):
        lftstr = ""
        rightstr = ""

        if self.left:
            lftstr = self.left.__str__()
        elif self.right:
            lftstr = "_"

        if self.right:
            rightstr = self.right.__str__()
        elif self.left:
            rightstr = "_"

        if self.root:
            rootstr = self.root.__str__()

        if (lftstr != "" or lftstr == "_") and (rightstr != "" or rightstr == "_"):
            finalstr = "[" + lftstr + " " +rootstr + " " + rightstr + "]"
        else:
            finalstr = "[" + lftstr + rootstr + rightstr + "]"
        return finalstr

    def __eq__(self, other):

        if self.left and other.left:
            lefteq = self.left.__eq__(other.left)
        elif self.left is None and other.left is None:
            lefteq = True
        elif self.left is None or other.left is None:
            lefteq = False

        if self.right and other.right:
            righteq = self.right.__eq__(other.right)
        elif self.right is None and other.right is None:
            righteq = True
        elif self.right is None or other.right is None:
            righteq = False

        if self.root and other.root:
            rooteq = self.root.__eq__(other.root)
        elif self.root is None and other.root is None:
            rooteq = True
        elif self.root is None or other.root is None:
            rooteq = False

        return lefteq and righteq and rooteq

    def __ne__(self, other):
        if self.left and other.left:
            lefteq = self.left.__ne__(other.left)
        elif self.left is None and other.left is None:
            lefteq = False
        elif self.left is None or other.left is None:
            lefteq = True

        if self.right and other.right:
            righteq = self.right.__ne__(other.right)
        elif self.right is None and other.right is None:
            righteq = False
        elif self.right is None or other.right is None:
            righteq = True

        if self.root and other.root:
            rooteq = self.root.__ne__(other.root)
        elif self.root is None and other.root is None:
            rooteq = False
        elif self.root is None or other.root is None:
            rooteq = True

        return lefteq or righteq or rooteq


if __name__ == '__main__':
    # test.describe('Example Test Cases -- Equality')

    # test.it('Equality -- Leaf')
    tree1 = Tree(Node('A'))
    tree2 = Tree(Node('A'))
    if tree1 == tree2:
        print("Equality -- Leaf: Trees are equal")
    else:
        print("Equality -- Leaf: Trees are not equal")
    # test.assert_equals(tree1 == tree2, True, "Failed tree equality")

    # test.it('Equality -- Balanced tree')
    tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    tree2 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    if tree1 == tree2:
        print("Equality -- Balanced tree: Trees are equal")
    else:
        print("Equality -- Balanced tree: Trees are not equal")
    # test.assert_equals(tree1 == tree2, True, "Failed tree equality")

    # test.it('Equality -- Missing subtrees')
    tree1 = Tree(Node('B'), None, Tree(Node('C')))
    tree2 = Tree(Node('B'), None, Tree(Node('C')))
    if tree1 == tree2:
        print("Equality -- Missing subtrees: Trees are equal")
    else:
        print("Equality -- Missing subtrees: Trees are not equal")
    # test.assert_equals(tree1 == tree2, True, "Failed tree equality")

    # test.describe('Example Test Cases -- Inequality')
    # test.it('Inequality -- Single node')
    tree1 = Tree(Node('A'))
    tree2 = Tree(Node('B'))
    if tree1 != tree2:
        print("Inequality -- Single node: Trees are not equal")
    else:
        print("Inequality -- Single node: Trees are equal")
    # test.assert_equals(tree1 != tree2, True, "Failed tree inequality")

    # test.it('Inequality -- Balanced tree')
    tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    tree2 = Tree(Node('B'), Tree(Node('A')), Tree(Node('D')))
    if tree1 != tree2:
        print("Inequality -- Balanced tree: Trees are not equal")
    else:
        print("Inequality -- Balanced tree: Trees are equal")

    # test.assert_equals(tree1 != tree2, True, "Failed tree inequality")
    #
    # test.it('Inequality -- Missing subtrees')
    tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    tree2 = Tree(Node('B'), None, Tree(Node('C')))
    if tree1 != tree2:
        print("Inequality -- Missing subtrees: Trees are not equal")
    else:
        print("Inequality -- Missing subtrees: Trees are equal")
    # test.assert_equals(tree1 != tree2, True, "Failed tree inequality")
    #
    # test.it('Inequality -- Same nodes, different structure')
    tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    tree2 = Tree(Node('A'), None, Tree(Node('C'), Tree(Node('B')), None))
    if tree1 != tree2:
        print("Inequality -- Same nodes, different structure: Trees are not equal")
    else:
        print("Inequality -- Same nodes, different structure: Trees are equal")
    # test.assert_equals(tree1 != tree2, True, "Failed tree inequality")
    #
    # test.describe('Example Test Cases -- String Representation')
    #
    # test.it('str -- Leaf')
    # print(str(Tree(Node('A')))) # expected '[A]'
    # test.assert_equals(str(Tree(Node('A'))), '[A]', 'Failed str')
    #
    # test.it('str -- Balanced tree')
    tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
    print(str(tree1))  # expected '[[A] B [C]]'
    # test.assert_equals(str(tree1), '[[A] B [C]]', 'Failed str')

    tree2 = Tree(Node('F'), Tree(Node('E')), Tree(Node('G')))
    print(str(tree2))  # expected '[[E] F [G]]'
    # test.assert_equals(str(tree2), '[[E] F [G]]', 'Failed str')

    tree3 = Tree(Node('D'), tree1, tree2)
    print(str(tree3))  # expected '[[[A] B [C]] D [[E] F [G]]]'
    # test.assert_equals(str(tree3), '[[[A] B [C]] D [[E] F [G]]]', 'Failed str')

    # test.it('str -- Missing subtrees')
    tree1 = Tree(Node('B'), None, Tree(Node('C')))
    print(str(tree1))  # expected '[_ B [C]]'
    # test.assert_equals(str(tree1), '[_ B [C]]', 'Failed str')
    tree2 = Tree(Node('F'), Tree(Node('E')), None)
    print(str(tree2)) # expected '[[E] F _]'
    # test.assert_equals(str(tree2), '[[E] F _]', 'Failed str')
    tree3 = Tree(Node('D'), tree1, tree2)
    print(str(tree3))  # expected '[[_ B [C]] D [[E] F _]]'
    # test.assert_equals(str(tree3), '[[_ B [C]] D [[E] F _]]', 'Failed str')
    tree4 = Tree(Node('F'), None, None)
    print(str(tree4)) # expected '[F]'
    # test.assert_equals(str(tree4), '[F]', 'Failed str')
    tree5 = Tree(Node('D'), tree1, tree4)
    print(str(tree5))  # expected '[[_ B [C]] D [F]]'
    # test.assert_equals(str(tree5), '[[_ B [C]] D [F]]', 'Failed str')
