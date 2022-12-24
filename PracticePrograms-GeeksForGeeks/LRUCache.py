# Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries.
# Query can be of two types:
# SET x y : sets the value of the key x with value y
# GET x : gets the key of x if present else returns -1.

# The LRUCache class has two methods get() and set() which are defined as follows.
# get(key)   :
# returns the value of the key if it already exists in the cache otherwise returns -1.
# set(key, value) :
# if the key is already present, update its value. If not present, add the key-value pair to the cache.
# If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
# In the constructor of the class the capacity of the cache should be initialized.

# design the class in the most optimal way

class Dnode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.clist = {}
        self.size = cap
        self.count = 0
        self.head = None
        self.tail = None

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.clist.keys():
            node = self.clist[key]
            self.removenode(node)
            self.updateheadnode(node)
            return node.value
        else:
            return -1

    def updateheadnode(self, inode):
        if self.head is None:
            self.head = inode
            self.tail = inode
        else:
            inode.next = self.head
            self.head.prev = inode
            self.head = inode

    def removenode(self, inode):
        if inode.next is not None and inode.prev is not None:
            inode.next.prev = inode.prev
            inode.prev.next = inode.next
        elif inode == self.head and inode == self.tail:
            self.head = None
            self.tail = None
        elif inode == self.head and inode.next is not None:
            self.head = inode.next
            self.head.prev = None
        elif inode == self.tail and inode.prev is not None:
            self.tail = inode.prev
            self.tail.next = None

    # Function for storing key-value pair.
    def set(self, key, value):
        if key in self.clist.keys():
            node = self.clist[key]
            node.value = value
            self.removenode(node)
            self.updateheadnode(node)
        else:
            node = Dnode(key, value)
            self.clist[key] = node
            if self.count < self.size:
                self.count += 1
                self.updateheadnode(node)
            else:
                r_key = self.tail.key
                self.removenode(self.tail)
                if r_key in self.clist.keys():
                    self.clist.pop(r_key)
                self.updateheadnode(node)


# code here

if __name__ == '__main__':
    cap = 2
    c2 = LRUCache(cap)
    c2.set(1, 2)
    print(c2.get(1))
    print("===============================")
    cap = 2
    c1 = LRUCache(cap)
    c1.set(1, 2)
    c1.set(2, 3)
    c1.set(1, 5)
    c1.set(4, 5)
    c1.set(6, 7)
    print(c1.get(4))
    c1.set(1, 2)
    print(c1.get(3))
