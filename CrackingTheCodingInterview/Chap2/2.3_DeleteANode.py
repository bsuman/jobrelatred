# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# input:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f


import SingleLinkedList as sll
import node as nc


# wrong solution as there is no access to the singly linked list
def removenode(ll: sll.singlell, rnc):
    assert (ll.head is not None and rnc is not None)
    start = ll.head
    while start.next is not None and start.next.data != rnc:
        start = start.next

    if start.next.data == rnc:
        start.next = start.next.next


# correct solution:

def removegivennode(rnc: nc.node):
    assert (rnc is not None and rnc.next is not None)
    rnc.data = rnc.next.data
    rnc.next = rnc.next.next



if __name__ == "__main__":
    ll = sll.singlell()
    ll.insert("f")
    ll.insert("e")
    ll.insert("d")
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.displayallvalues()
    start = ll.head
    while start.data != "c":
        start = start.next
    if start.data == "c":
        removegivennode(start)
    print("===============================")
    ll.displayallvalues()
