# Given a binary tree, print the level order traversal in such a way that first two levels are printed from left to right,
# next two levels are printed from right to left, then next two from left to right and so on.
# So, the problem is to reverse the direction of level order traversal of binary tree after every two levels.


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

    def level_order_dir_change(self):
        if self is None:
            return
        elif self.left is None and self.right is None:
            return [self.data]

        queue = [self]
        stack = []
        l_o_d = []
        rtol = False
        count = 0
        while len(queue) > 0:
            count = count + 1
            num = len(queue)
            for i in range(num):
                current = queue.pop(0)
                if not rtol:
                    l_o_d.append(current.data)
                else:
                    stack.insert(0,current.data)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            if rtol:
                while len(stack) > 0:
                    l_o_d.append(stack.pop(0))
            if count == 2:
                rtol = not rtol
                count = 0
        return l_o_d

if __name__ == '__main__':
    root = node(0)
    for i in range(1, 20):
        root.insert(i)
    l = root.level_order_dir_change()
    print(l)
