# Given the head of a singly linked list, reverse the list, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head is None:
        return None
    elif head.next is None:
        return head

    start = head
    stack = []
    while start is not None:
        stack.insert(0, start)
        start = start.next

    newhead = stack.pop(0)
    node = newhead
    while len(stack) > 0:
        nextnode = stack.pop(0)
        node.next = nextnode
        node = nextnode

    node.next = None
    return newhead


if __name__ == '__main__':
    l1 = [1,2]
    list1 = ListNode(l1[0])
    start = list1
    for i in range(1, len(l1)):
        lnode = ListNode(l1[i])
        start.next = lnode
        start = lnode

    list1 = reverseList(list1)
    start = list1
    l = []
    while start is not None:
        l.append(start.val)
        start = start.next

    print(l)