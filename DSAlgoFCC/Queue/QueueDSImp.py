# Implementation of queue data structure ( LiFo)
# 1. using lists
# 2. using linked list

# supporting functions:
# remove: removes the first item in the queue
# add: adds the item to the end of the queue
# peek: reads the first item in the queue and return the item
# isEmpty: function to check if the queue is empty

class myqueue:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self):
        if not self.isEmpty():
            self.data.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0


class node:
    def __init__(self, idata):
        self.data = idata
        self.next = None


class myqueuell:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        if self.first is None:
            self.first = item
            self.last = self.first
        else:
            self.last.next = item
            self.last = item

    def remove(self):
        if self.first is None:
            return "Queue Empty!"
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

    def peek(self):
        if self.first is None:
            return "Queue Empty!"
        else:
            return self.first.data

    def isEmpty(self):
        return self.first is None and self.last is None


if __name__ == '__main__':
    mq = myqueue()
    print(mq.isEmpty())
    mq.add(4)
    mq.add(5)
    mq.add(6)
    print(mq.isEmpty())
    print(mq.peek())
    mq.remove()
    print(mq.peek())
    print(mq.isEmpty())
    mq.remove()
    mq.remove()
    print(mq.isEmpty())
    print("================")
    mql = myqueuell()
    print(mql.isEmpty())
    mql.add(node(4))
    mql.add(node(5))
    mql.add(node(6))
    print(mql.isEmpty())
    print(mql.peek())
    mql.remove()
    print(mql.peek())
    mql.add(node(8))
    print(mql.isEmpty())
    mql.remove()
    print(mql.peek())
    mql.remove()
    print(mql.peek())
    print(mql.isEmpty())
