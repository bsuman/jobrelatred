# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    start = head
    # if last node should be deleted and there is one node in the list, return None
    if n == 1 and start.next is None:
        return None
    start = head
    len = 0
    while start is not None:
        start = start.next
        len = len + 1

    start = head
    if len == n:
        head = start.next
    else:
        for i in range(len - n - 1):
            start = start.next

        if start is not None and start.next is not None:
            start.next = start.next.next

    return head


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]
    head = ListNode(li[0])
    start = head
    for i in range(1, len(li)):
        lnode = ListNode(li[i])
        start.next = lnode
        start = start.next
    removeNthFromEnd(head, 2)
    start = head
    while start is not None:
        print(start.val)
        start = start.next
