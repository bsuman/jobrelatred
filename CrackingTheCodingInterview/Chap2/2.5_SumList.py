# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
import SingleLinkedList as sl


def sumlist(l1: sl.singlell, l2: sl.singlell):
    if l1.isEmpty():
        return l2
    elif l2.isEmpty():
        return l1
    num1 = l1.head
    num2 = l2.head
    fl = sl.singlell()
    carry = 0
    while True:
        x1 = None
        x2 = None
        if num1 is not None:
            x1 = num1.data
            num1 = num1.next
        if num2 is not None:
            x2 = num2.data
            num2 = num2.next
        if x1 is not None and x2 is not None:
            num = (x1 + x2 + carry)
            carry = num // 10
        elif x1 is None:
            num = x2
        elif x2 is None:
            num = x1

        fl.insertattail(num % 10)
        if num1 is None and num2 is None:
            return fl


# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

def getnum(l1: sl.singlell):
    start = l1.head
    n1, places = 0, 0
    while start.next is not None:
        places = places + 1
        start = start.next
    start = l1.head
    for i in range(places, -1, -1):
        n1 = n1 + start.data * (10 ** i)
        start = start.next

    return n1


def fsumlist(l1: sl.singlell, l2: sl.singlell):
    if l1.isEmpty():
        return l2
    elif l2.isEmpty():
        return l1
    n1, n2 = 0, 0
    n1 = getnum(l1)
    n2 = getnum(l2)
    fn = n1+n2
    numlis = list(str(fn))
    fl = sl.singlell()

    for i in numlis:
        fl.insertattail(   i)
    return fl


if __name__ == "__main__":
    num1 = sl.singlell()
    # (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
    num1.insert(6)
    num1.insert(1)
    num1.insert(7)

    num2 = sl.singlell()
    num2.insert(2)
    num2.insert(9)
    num2.insert(5)
    num3 = sumlist(num1, num2)
    num3.displayallvalues()

    num4 = sl.singlell()
    num4.insert(6)
    num4.insert(1)
    num5 = sl.singlell()
    num5.insert(4)
    num6 = sumlist(num4, num5)
    num6.displayallvalues()

    # lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
    # Output: 9 -> 1 -> 2. That is, 912.

    l1 = sl.singlell()
    l1.insertattail(6)
    l1.insertattail(1)
    l1.insertattail(7)
    l2 = sl.singlell()
    l2.insertattail(2)
    l2.insertattail(9)
    l2.insertattail(5)
    l3 = fsumlist(l1,l2)
    l3.displayallvalues()
