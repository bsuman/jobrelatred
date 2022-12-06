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
