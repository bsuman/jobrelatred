# Given a Binary Tree, write an iterative function to print the Preorder traversal of the given binary tree.


class node:
    def __init__(self, idata):
        self.data = idata
        self.right = None
        self.left = None

    def insert(self, val):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = node(val)
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = node(val)
                break
            else:
                queue.append(current.right)

    def inorder_traversal_iter(self):
        inorder = []
        Stack = []
        current = self
        while True:
            while current is not None:
                Stack.insert(0, current)
                current = current.left

            if current is None and len(Stack) == 0:
                return inorder
            elif current is None and len(Stack) > 0:
                current = Stack.pop(0)
                inorder.append(current.data)
                current = current.right
        return inorder

    def preorder_traversal_iter(self):
        preorder = []
        stack = [self]

        while len(stack) > 0:
            current = stack.pop(0)
            preorder.append(current.data)
            if current.right is not None:
                stack.insert(0, current.right)
            if current.left is not None:
                stack.insert(0, current.left)
        return preorder

    def postorder_traversal_iter(self):
        post_order = []
        stack = [self]
        stack2 = []
        while len(stack):
            current = stack.pop(0)
            if current:
                stack2.insert(0,current)
            if current.left is not None:
                stack.insert(0,current.left)
            if current.right is not None:
                stack.insert(0,current.right)

        while len(stack2):
            post_order.append(stack2.pop(0).data)

        return post_order

if __name__ == '__main__':
    root = node(1)
    for i in range(2, 14):
        root.insert(i)

    print(root.preorder_traversal_iter())
    print(root.postorder_traversal_iter())