# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks

class node:
    def __init__(self, idata):
        self.data = idata
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        newnode = node(val)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.size = self.size + 1

    def pop(self):
        if self.top is None:
            return "Empty Stack!"
        else:
            data = self.top.data
            self.top = self.top.next
            self.size = self.size - 1
            return data

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return "Empty Stack!"

    def isEmpty(self):
        return self.top is None

    def getsize(self):
        return self.size


class MyQueue:
    def __init__(self):
        self.front = stack()
        self.back = stack()

    def add(self, val):
        self.back.push(val)

    def updatestack(self):
        if self.front.top is None:
            while self.back.top is not None:
                self.front.push(self.back.pop())

    def remove(self):
        self.updatestack()
        return self.front.pop()

    def peek(self):
        self.updatestack()
        self.front.peek()


if __name__ == "__main__":
    mq = MyQueue()
    for i in range(1,6):
        mq.add(i)
    for i in range(1,3):
        print(mq.remove())

    for i in range(6, 8):
        mq.add(i)

    for i in range(1,6):
        print(mq.remove())