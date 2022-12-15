# Level order traversal line by line | Set 3 (Using One Queue)
# Given a Binary Tree, print the nodes level-wise, each level on a new line.

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

    def level_order_lineByline(self):
        queue = [self]
        while len(queue) > 0:
            num = len(queue)
            tstr = ""
            for i in range(num):
                current = queue.pop(0)
                if current is not None:
                    if tstr == "":
                        tstr = str(current.data)
                    else:
                        tstr = tstr + " " + str(current.data)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            if tstr != "":
                print(tstr)


if __name__ == '__main__':
    root = node(0)
    for i in range(1, 20):
        root.insert(i)

    root.level_order_lineByline()

    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.right = node(6)
    root.level_order_lineByline()