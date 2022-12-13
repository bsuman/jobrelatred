# Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and is Empty.


class node:
    def __init__(self, idata):
        self.data = idata
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        newnode = node(val)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top is None:
            return "Empty Stack!"
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return "Empty Stack!"

    def isEmpty(self):
        return self.top is None


class sortedstack(stack):
    def __init__(self):
        super().__init__()

    def push(self, val):
        if super().isEmpty():
            super().push(val)
            return

        if super().peek() >= val:
            super().push(val)
        else:
            tempstack = stack()
            start = self.top
            while start is not None:
                if super().peek() < val:
                    tempstack.push(super().pop())
                else:
                    break
                start = start.next

            tempstack.push(val)
            start = tempstack.top
            while start is not None:
                super().push(tempstack.pop())
                start = start.next


if __name__ == '__main__':
    s = sortedstack()
    s.push(30)
    s.push(23)
    s.push(42)
    print(s.peek())
    s.push(38)
    print(s.peek())
    s.push(13)
    print(s.peek())
    s.push(12)
    print(s.peek())
    s.push(50)
    print(s.peek())
    s.push(2)
    print(s.peek())

    while s.top is not None:
        print(s.pop())