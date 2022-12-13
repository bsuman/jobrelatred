# Implement single linked list with the following functions
# insert: insert element at the start of the list
# insertatpos: insert element at the given position
# remove: remove the element at the start of the list
# removeatpos: remove the element at the given position
# removevalue: remove the first node with the given value
# getvalatpos: get the element at the given position
# getposofval: returns the position of the first occurence of the given value
# displayallvalues: displays all the values in the linked list

from CrackingTheCodingInterview.Chap2 import node as nc


class singlell:
    def __init__(self):
        self.head = None
        self.size = 0

    # insert element at the start of the list
    def insert(self, val):
        inode = nc.node(val)
        if self.isEmpty():
            self.head = inode
        else:
            inode.next = self.head
            self.head = inode

    def insertattail(self,val):
        inode = nc.node(val)
        if self.isEmpty():
            self.head = inode
        else:
            start = self.head
            while start.next is not None:
                start = start.next
            start.next = inode

    # insert element at the given position
    def insertatpos(self, val, pos):
        inode = nc.node(val)
        if self.isEmpty() and pos > 0:
            return "Position not found, list is empty!"
        else:
            num = 0
            if pos == num:
                inode.next = self.head
                self.head = inode
            else:
                start = self.head
                while start.next is not None:
                    num = num + 1
                    if num == pos:
                        inode.next = start.next
                        start.next = inode
                        return "Value inserted!"
                    start = start.next
                return "Position not found !"

    # remove the element at the start of the list
    def remove(self):
        if self.isEmpty() is None:
            return "List is empty!"
        else:
            val = self.head.data
            self.head = self.head.next
            return val

    # remove the first occurrence with the given value
    def removevalue(self, val):
        if self.isEmpty():
            return "List is empty!"
        else:
            if self.head.data == val:
                self.head = self.head.next
                return "First occurrence of the value removed!"
            else:
                start = self.head
                while start.next is not None:
                    if start.next.data == val:
                        start.next = start.next.next
                        return "First occurrence of the value removed!"
                    start = start.next
                return "Value not found!"

    # remove the element at the given position
    def removeatpos(self, pos):
        if self.isEmpty() and pos > 0:
            return "List is Empty, position not found!"
        else:
            num = 0
            if pos == num:
                val = self.head.data
                self.head = self.head.next
                return val
            else:
                start = self.head
                while start.next is not None:
                    num = num + 1
                    if num == pos:
                        val = start.next.data
                        start.next = start.next.next
                        return val
                    start = start.next
                return "Position not found!"

    def getvalatpos(self, pos):
        if self.isEmpty() and pos > 0:
            return "List is Empty, position not found!"
        else:
            num = 0
            if pos == num:
                return self.head.data
            else:
                start = self.head
                while start.next is not None:
                    num = num + 1
                    if num == pos:
                        return start.data
                    start = start.next
                return "Position not found!"

    def getposofval(self, value):
        if self.isEmpty():
            return "List is Empty, value not found!"
        else:
            pos = 0
            if self.head.data == value:
                return pos
            else:
                start = self.head
                while start.next is not None:
                    if start.data == value:
                        return pos
                    pos = pos + 1
                    start = start.next
                return "Value not found!"

    def displayallvalues(self):
        if self.isEmpty():
            print("List is Empty!")
        else:
            start = self.head
            while start is not None:
                print("Value = {}".format(start.data))
                start = start.next
            return "All items displayed!"

    def isEmpty(self):
        return self.head is None


if __name__ == '__main__':
    sll = singlell()
    print(sll.isEmpty())
    sll.insert(10)
    sll.insertatpos(12,1)
    sll.insert(12)
    print(sll.isEmpty())
    print(sll.displayallvalues())
    sll.insertatpos(22,1)
    print(sll.displayallvalues())
    sll.removeatpos(1)
    print(sll.displayallvalues())
    sll.removevalue(10)
    print(sll.displayallvalues())
    sll.insert(112)
    sll.insert(212)
    print(sll.getposofval(112))
    print(sll.getvalatpos(2))
    print(sll.getvalatpos(0))