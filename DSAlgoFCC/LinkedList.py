# Linked List
# A linked list is a data structure used for storing a sequence of elements. It's data with some structure (the sequence).
# Implement linked lists which support the following operations:
#
# Create a list with given elements
# Display the elements in a list
# Find the number of elements in a list
# Retrieve the element at a given position
# Add or remove element(s)

class Node:
    def __init__(self, ivalue=None):
        self.value = ivalue
        self.next = None


class LinkedList:
    def __init__(self, inode=None):
        self.node = inode

    def insert(self, node):
        if self.node is None:
            self.node = node
            return
        start = self.node
        while start.next is not None:
            start = start.next
        start.next = node


    def display(self):
        if self.node is None:
            return
        start = self.node
        while start is not None:
            print(start.value)
            start = start.next

    def delete(self, ivalue):
        if self.node is not None and self.node.value == ivalue:
            self.node.value = self.node.next.value
            self.node.next = self.node.next.next
            return
        start = self.node
        while start is not None and start.next is not None:
            if start.next.value == ivalue:
                start.next = start.next.next
                return
            start = start.next

    def size(self):
        num = 0
        start = self.node
        while start is not None:
            num = num+1
            start = start.next
        return num

    def getElementAtPos(self,pos):
        currpos =0
        start = self.node
        while start is not None:
            if currpos == pos:
                return start.value
            currpos = currpos + 1
            start = start.next



def reverselist(l):
    start = l.node
    if start is None:
        return
    currentnode = start
    previousnode = None
    while currentnode is not None:
        nextnode = currentnode.next
        currentnode.next = previousnode
        previousnode = currentnode
        currentnode = nextnode

    l.node = previousnode

if __name__ == '__main__':
    ll = LinkedList()
    node1 = Node(4)
    ll.insert(node1)
    node2 = Node(7)
    ll.insert(node2)
    node3 = Node(14)
    ll.insert(node3)
    node4 = Node(17)
    ll.insert(node4)
    node5 = Node(42)
    ll.insert(node5)
    node6 = Node(71)
    print("==========================================")
    ll.insert(node6)
    ll.display()
    print("==========================================")
    print(ll.size())
    print("==========================================")
    ll.delete(17)
    ll.display()
    print("==========================================")
    print(ll.size())
    print("==========================================")
    print(ll.getElementAtPos(2))
    print("==========================================")
    ll.delete(4)
    ll.display()
    print("==========================================")
    reverselist(ll)
    ll.display()
    print("==========================================")