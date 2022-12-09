# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

import SingleLinkedList as sl


def getKthElementToLast(sll: sl.singlell, k: int):
    if sll.isEmpty():
        print("List is Empty!")
        return
    start = sll.head
    while start is not None:
        runner = start
        for i in range(k):
            runner = runner.next
            if runner is None:
                return "K is too large!"
        if runner.next is None:
            return start.data
        start = start.next


if __name__ == "__main__":
    slinklist = sl.singlell()
    for i in range(11):
        slinklist.insert(i)

    print(getKthElementToLast(slinklist,4))
    print(getKthElementToLast(slinklist,1))
    print(getKthElementToLast(slinklist,10))
    print(getKthElementToLast(slinklist,11))
    print(getKthElementToLast(slinklist,0))