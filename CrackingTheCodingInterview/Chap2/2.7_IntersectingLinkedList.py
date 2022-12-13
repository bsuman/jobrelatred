# Intersection: Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# constraints:
# worst case time complexity: O(A+B) [A- length of linked list 1 and B- length of linked list 2]
# worst case space complexity is O(1)

# if the linked lists are intersecting, after the intersecting node, the list is the same.
# So to check if the lists are intersecting, check if both the lists have the same node the end.
# If yes, then continue to get the intersecting node

import SingleLinkedList as sll
from CrackingTheCodingInterview.Chap2 import node as nc


def CheckifIntersecting(ll1: sll.singlell, ll2: sll.singlell):
    assert (not ll1.isEmpty() and not ll2.isEmpty())
    start1 = ll1.head
    ll1_size = 0
    while start1.next is not None:
        ll1_size = ll1_size + 1
        start1 = start1.next

    ll1_size = ll1_size + 1
    ll1_lnode = start1

    start2 = ll2.head
    ll2_size = 0
    while start2.next is not None:
        ll2_size = ll2_size + 1
        start2 = start2.next

    ll2_size = ll2_size + 1
    ll2_lnode = start2
    if ll2_lnode != ll1_lnode:
        return False
    else:
        inc_counter = 0
        start2 = ll2.head
        start1 = ll1.head
        if ll1_size > ll2_size:
            inc_counter = ll1_size - ll2_size
            for i in range(inc_counter):
                start1 = start1.next
        elif ll2_size > ll1_size:
            inc_counter = ll2_size - ll1_size
            for i in range(inc_counter):
                start2 = start2.next
        while start1 != start2:
            start1 = start1.next
            start2 = start2.next

        return start1


if __name__ == '__main__':
    ll1 = sll.singlell()
    for i in range(10):
        ll1.insertattail(i)
    ll2 = sll.singlell()
    ll2.insert(12)
    ll2.insert(13)
    ll2.insert(14)
    start = ll1.head
    start2 = ll2.head
    for i in range(2):
        start = start.next
        start2 = start2.next

    start2.next = start
    ll1.displayallvalues()
    print("=======================================")
    ll2.displayallvalues()
    returnval = CheckifIntersecting(ll1,ll2)
    print("=======================================")
    if type(returnval) is nc.node:
        print("Intersecting node is = {}".format(returnval.data))
    else:
        print("Not interesecting!")