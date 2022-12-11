# Palindrome: Implement a function to check if a linked list is a palindrome.

import SingleLinkedList as sl


def checkpalindrome(l1: sl.singlell) -> bool:
    if l1.isEmpty():
        return False
    elif l1.head.data != 1 and l1.head.next is None:
        return False
    elif l1.head.data != 1 or (l1.head.next.data != 1 and l1.head.next.next is None):
        return False
    else:
        f0 = l1.head
        f1 = l1.head.next
        while f1 is not None and f1.next is not None:
            f2 = f1.next
            if f2.data != (f0.data + f1.data):
                return False
            f0 = f1
            f1 = f2
        return True


if __name__ == "__main__":
    ll = sl.singlell()
    ll.insertattail(1)
    ll.insertattail(1)
    ll.insertattail(2)
    ll.insertattail(3)
    ll.insertattail(5)
    ll.displayallvalues()
    if checkpalindrome(ll):
        print("is palindrome!")
    else:
        print("is not a palindrome!")

    ll1 = sl.singlell()
    ll1.insertattail(1)
    ll1.insertattail(0)
    if checkpalindrome(ll1):
        print("is palindrome!")
    else:
        print("is not a palindrome!")

