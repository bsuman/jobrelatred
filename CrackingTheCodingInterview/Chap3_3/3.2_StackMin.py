# Design and Implement a stack which, in addition to push and pop, has a function minValue which returns the minimum element
# Constraint: Push, pop, min should all operation in O(1) time

class snode:
    def __init__(self, idata):
        self.data = idata
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = snode(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print("Stack is Empty")

    def isEmpty(self):
        return self.top is None


class minstack(stack):
    def __init__(self):
        self.minSt = stack()
        super().__init__()

    def push(self, item):
        minval = self.minSt.peek()
        if minval is not None and minval > item:
            self.minSt.push(item)
        elif minval is None:
            self.minSt.push(item)
        super().push(item)

    def minValue(self):
        return self.minSt.peek()

    def pop(self):
        if super().pop() == self.minSt.peek():
            self.minSt.pop()


if __name__ == "__main__":
    nstack = minstack()
    nstack.push(30)
    print(nstack.minValue())
    nstack.push(40)
    print(nstack.minValue())
    nstack.push(50)
    print(nstack.minValue())
    nstack.push(5)
    print(nstack.minValue())
    nstack.pop()
    print(nstack.minValue())