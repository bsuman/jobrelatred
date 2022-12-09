# Remove Dups! Write code to remove duplicates from an unsorted linked list.

import SingleLinkedList as sll

def removeDuplicatesWithBuf(ll:sll.singlell):
    if ll.isEmpty():
        print("List is empty, no duplicates")
        return

    start = ll.head
    dic = {start.data: "True"}
    while start.next is not None:
        if start.next.data in dic.keys():
            start.next = start.next.next
        else:
            dic[start.next.data] = True
            start = start.next



# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
def removeduplicates(ll:sll.singlell):
    if ll.isEmpty():
        print("List is empty, no duplicates")
        return

    start = ll.head
    while start.next is not None:
        data = start.data
        nextStart = start
        while nextStart is not None and nextStart.next is not None:
            if nextStart.next.data == data:
                nextStart.next = nextStart.next.next
            nextStart = nextStart.next
        start = start.next

if __name__ == "__main__":
    tmp = sll.singlell()
    tmp.insert(10)
    tmp.insert(20)
    tmp.insert(10)
    tmp.insert(40)
    tmp.insert(20)
    tmp.insert(10)
    tmp.displayallvalues()
    print("====================================")
    removeduplicates(tmp)
    tmp.displayallvalues()
    print("====================================")
    tmp2 = sll.singlell()
    tmp2.displayallvalues()
    removeduplicates(tmp2)
    print("====================================")
    tmp3 = sll.singlell()
    tmp3.insert(10)
    tmp3.displayallvalues()
    removeduplicates(tmp3)
    tmp3.displayallvalues()
    print("====================================")
    tmp4 = sll.singlell()
    tmp4.insert(10)
    tmp4.insert(20)
    tmp4.insert(40)
    tmp4.insert(10)
    tmp4.insert(20)
    tmp4.insert(200)
    tmp4.insert(20)
    print("======== Before Remove ============")
    tmp4.displayallvalues()
    removeDuplicatesWithBuf(tmp4)
    print("======== After Remove ============")
    tmp4.displayallvalues()

