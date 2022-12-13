# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

import SingleLinkedList as sl
from CrackingTheCodingInterview.Chap2 import node as nc


# implementing floyd's Loop detection algorithm
def detectloop(ll: sl.singlell):
    assert (not ll.isEmpty())
    start = ll.head
    runner = ll.head
    while runner is not None and runner.next is not None:
        start = start.next
        runner = runner.next.next
        if start == runner:
            break

    if runner is None or runner.next is None:
        return False

    start = ll.head
    while start != runner:
        start = start.next
        runner = runner.next

    return start


if __name__ == '__main__':
    ll1 = sl.singlell()
    for i in range(10):
        ll1.insertattail(i)

    start = ll1.head
    loop = start.next.next.next.next
    while start.next is not None:
        start = start.next

    start.next = loop

    result = detectloop(ll1)
    if type(result) is nc.node:
        print("The loop is formed at = {}".format(result.data))
    else:
        print("No Loop!")
