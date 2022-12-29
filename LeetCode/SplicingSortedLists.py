# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1 is None and list2 is None:
        return []

    retval = None
    start = None
    lookup = None
    if list1.val <= list2.val:
        start = list1
        retval = list1
        lookup = list2
    else:
        start = list2
        retval = list2
        lookup = list1

    while True:
        while start.next is not None and start.next.val < lookup.val:
            start = start.next

        if start.next is not None and start.next.val >= lookup.val:
            tmp = start.next
            start.next = lookup
            start = lookup
            lookup = tmp
        elif start.next is None:
            if start.val <= lookup.val:
                start.next = lookup
                break
    return retval


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    list1 = ListNode(l1[0])
    start = list1
    for i in range(1, len(l1)):
        lnode = ListNode(l1[i])
        start.next = lnode
        start = lnode

    list2 = ListNode(l2[0])
    start = list2
    for i in range(1, len(l2)):
        lnode = ListNode(l2[i])
        start.next = lnode
        start = lnode

    list3 = mergeTwoLists(list1, list2)
    start = list3
    l = []
    while start is not None:
        l.append(start.val)
        start = start.next

    print(l)
