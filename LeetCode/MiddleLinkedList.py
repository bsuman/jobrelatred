# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    start = head
    runner = start
    while start is not None and start.next is not None:
        runner = runner.next.next
        start = start.next
        if runner is None or runner.next is None:
            break

    if runner is None:
        return start

