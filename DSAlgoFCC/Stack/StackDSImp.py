# Stack implementation
# 1. using lists
# 2. using linked list

# supporting functions:
# pop: removes the first item in the stack
# push: adds the item to the top of the stack
# peek: reads the element from the top of the stack and return the element
# isEmpty: function to check if the stack is empty
class StackEmptyError(Exception):
    pass


class Mystack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)
        print("Item = {} pushed to the stack".format(item))

    def pop(self):
        try:
            return self.stack.pop(0)
        except:
            print("Stack is empty!")

    def peek(self):
        try:
            return self.stack[0]
        except:
            print("Stack is empty!")

    def isEmpty(self):
        return len(self.stack) == 0


# ===========================================================================================================
class stacknode:
    def __init__(self, item):
        self.data = item
        self.next = None


class mystackll:
    def __init__(self):
        self.top = None

    def push(self, item):
        if self.top is None:
            self.top = item
        else:
            item.next = self.top
            self.top = item

    def pop(self):
        try:
            if self.top is None:
                raise StackEmptyError
            else:
                data = self.top.data
                if self.top.next is not None:
                    self.top = self.top.next
                else:
                    self.top = None
                return data
        except StackEmptyError:
            print("Stack is empty!")

    def peek(self):
        try:
            if self.top:
                return self.top.data
            else:
                raise StackEmptyError
        except StackEmptyError:
            print("Stack is empty!")

    def isEmpty(self):
        return self.top is None


if __name__ == '__main__':
    mstack = Mystack()
    mstack.push(10)
    mstack.push(20)
    mstack.push(40)
    mstack.push(30)
    print(mstack.isEmpty())
    print(mstack.peek())
    print(mstack.pop())
    print(mstack.peek())
    print(mstack.pop())
    print(mstack.peek())
    print(mstack.pop())
    print(mstack.pop())
    print(mstack.peek())
    print(mstack.isEmpty())

    myllstack = mystackll()
    node1 = stacknode("a")
    myllstack.push(node1)
    node1 = stacknode("b")
    myllstack.push(node1)
    node1 = stacknode("c")
    myllstack.push(node1)
    node1 = stacknode("d")
    myllstack.push(node1)
    print(myllstack.isEmpty())
    print(myllstack.peek())
    print(myllstack.pop())
    print(myllstack.peek())
    print(myllstack.pop())
    print(myllstack.peek())
    print(myllstack.pop())
    print(myllstack.pop())
    print(myllstack.peek())
    print(myllstack.isEmpty())