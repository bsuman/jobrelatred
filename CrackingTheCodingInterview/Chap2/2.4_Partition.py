# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# 3->43->23->5->12->0->8->108->54 [partition= 5]
# 3->0->23->5->12->43->8->108->54


# 9->8->1->2->5->4->3->6->12 [partition= 9]
# 8->9->1->2->5->4->3->6->12
# 8->1->9->2->5->4->3->6->12
# 8->1->2->9->5->4->3->6->12
# 8->1->2->5->9->4->3->6->12
# 8->1->2->5->4->9->3->6->12
# 8->1->2->5->4->3->9->6->12
# 8->1->2->5->4->3->6->9->12

# 9->8->1->2->5->4->3->6->12 [partition= 9]
# 9->8->1->2->5->4->3->6->12 [9 compare 12]
# 6->8->1->2->5->4->3->9->12 [9 compare 6 ?, swap]
# 6->8->1->2->5->4->3->9->12 [8 compare 9, 3 compare 9 ?]
# 6->8->1->2->5->4->3->9->12 [1 compare 9, 3 compare 9 ?]

import SingleLinkedList as sll


def partition(ll: sll.singlell, val: int):
    assert (not ll.isEmpty())
    start = ll.head
    while start.next is not None:
        if start.data >= val:
            snode = start.next
            bnode = None
            while snode.next is not None:
                if snode.data < val:
                    bnode = snode
                snode = snode.next

            if snode.data < val:
                tmp = start.data
                start.data = snode.data
                snode.data = tmp
            elif bnode is not None:
                tmp = start.data
                start.data = bnode.data
                bnode.data = tmp
        start = start.next


if __name__ == '__main__':
    ll = sll.singlell()
    # 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    ll.insert(1)
    ll.insert(2)
    ll.insert(10)
    ll.insert(5)
    ll.insert(8)
    ll.insert(5)
    ll.insert(3)
    ll.displayallvalues()
    partition(ll, 5)
    print("================================================")
    ll.displayallvalues()
    # 9->8->1->2->5->4->3->6->12 [partition= 9]
    nll = sll.singlell()
    nll.insert(12)
    nll.insert(6)
    nll.insert(3)
    nll.insert(4)
    nll.insert(5)
    nll.insert(2)
    nll.insert(1)
    nll.insert(8)
    nll.insert(9)
    print("================================================")
    nll.displayallvalues()
    partition(nll, 9)
    print("================================================")
    nll.displayallvalues()
    # 3->0->23->5->12->0->8->108->54 [partition= 5]
    # 3->0->0->5->12->23->8->108->54
    nll1 = sll.singlell()
    nll1.insert(54)
    nll1.insert(108)
    nll1.insert(8)
    nll1.insert(0)
    nll1.insert(12)
    nll1.insert(5)
    nll1.insert(23)
    nll1.insert(0)
    nll1.insert(3)
    print("================================================")
    nll1.displayallvalues()
    partition(nll1, 5)
    print("================================================")
    nll1.displayallvalues()
