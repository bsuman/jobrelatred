# Given a Binary Tree, the task is to print the Level order traversal of the Binary Tree in spiral form i.e, alternate order.

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

    def level_order_spiral(self):
        level_order_spiral = []
        queue = [self]
        level = 0
        while len(queue):
            tmp= []
            num = len(queue)
            for i in range(num):
                current = queue.pop(0)
                if current is not None:
                    level_order_spiral.append(current.data)
                if level % 2 == 1:
                    if current.left is not None:
                        tmp.insert(0, current.left)
                    if current.right is not None:
                        tmp.insert(0, current.right)
                else:
                    if current.right is not None:
                        tmp.insert(0, current.right)
                    if current.left is not None:
                        tmp.insert(0, current.left)
            queue = tmp
            level = level + 1
        return level_order_spiral

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(7)
    root.left.right = node(6)
    root.right.left = node(5)
    root.right.right = node(4)
    print(root.level_order_spiral())

    root = node(0)
    for i in range(1, 20):
        root.insert(i)

    print(root.level_order_spiral())