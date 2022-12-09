# Implement doubly linked list with the following functions
# insert: insert element at the start of the list
# insertatpos: insert element at the given position
# remove: remove the element at the start of the list
# removeatpos: remove the element at the given position
# removevalue: remove the first node with the given value
# displayallvalues: displays all the values in the linked list

import node


class doublyll:
    def __init__(self):
        self.head = None

    def insert(self, val):
        inode = node.dnode(val)
        if self.isEmpty():
            self.head = inode
            return
        else:
            inode.next = self.head
            self.head.prev = inode
            self.head = inode

    def insertatpos(self, pos, val):
        if self.isEmpty() and pos > 0:
            return "List is empty, position not found!"
        else:
            if pos == 0:
                self.insert(val)
            else:
                inode = node.dnode(val)
                start = self.head
                num = 0
                while start.next is not None:
                    num = num + 1
                    if num == pos:
                        inode.next = start.next
                        start.next.prev = inode
                        start.next = inode
                        inode.prev = start
                        return "Val = {} inserted at pos = {}".format(val, pos)
                    start = start.next
                return "Position not found!"

    def remove(self):
        if self.isEmpty():
            return "List is empty!"
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeatpos(self, pos):
        if self.isEmpty():
            return "List is empty!"
        else:
            if pos == 0:
                self.remove()
            else:
                num = 0
                start = self.head
                while start.next is not None:
                    num = num + 1
                    if num == pos:
                        start.next = start.next.next
                        if start.next is not None:
                            start.next.prev = start
                        return
                    start = start.next
                return "Position not found!"

    def removevalue(self, val):
        if self.isEmpty():
            return "List is empty!"
        else:
            if self.head.data == val:
                self.remove()
            else:
                start = self.head
                while start.next is not None:
                    if start.data == val:
                        start.next = start.next.next
                        if start.next is not None:
                            start.next.prev = start
                        return
                    start = start.next
                return "Value not found!"

    def displayallvalues(self):
        if self.isEmpty():
            return "List is empty!"
        else:
            start = self.head
            while start is not None:
                print("The value is {}".format(start.data))
                start = start.next

    def isEmpty(self):
        return self.head is None


if __name__ == "__main__":
    dll = doublyll()
    print(dll.isEmpty())
    dll.insert(12)
    dll.displayallvalues()
    dll.insert(22)
    dll.displayallvalues()
    dll.insertatpos(1, 34)
    dll.displayallvalues()
    dll.remove()
    dll.displayallvalues()
    dll.removevalue(34)
    dll.displayallvalues()
    dll.insert(200)
    dll.insert(400)
    dll.displayallvalues()
    dll.removeatpos(1)
    dll.displayallvalues()

