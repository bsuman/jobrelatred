# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold.

# Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).


# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack

class node:
    def __init__(self, idata):
        self.data = idata
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.nextStack = None

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


class SetOfStacks:
    def __init__(self, icapacity):
        self.currstack = stack()
        self.capacity = icapacity

    def push(self, i):
        if self.currstack.getsize() < self.capacity:
            self.currstack.push(i)
        else:
            newstack = stack()
            newstack.nextStack = self.currstack
            self.currstack = newstack
            self.currstack.push(i)

    def pop(self):
        if self.currstack is None:
            return "No Stacks"
        else:
            if self.currstack.getsize() > 0:
                return self.currstack.pop()
            else:
                self.currstack = self.currstack.nextStack
                if self.currstack is not None:
                    return self.currstack.pop()
                else:
                    return "No Stacks Left!"

    def popAt(self, i):
        j = 0
        start = self.currstack
        while j <= i-1:
            start = start.nextStack
            j = j + 1
        if start is not None:
            return start.pop()

if __name__ == '__main__':
    sos = SetOfStacks(5)
    for i in range(1, 12):
        sos.push(i)
    print(sos.popAt(1))
    for i in range(6):
        print(sos.pop())


