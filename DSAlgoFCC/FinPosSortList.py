# QUESTION 1: Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# Problem Definition: Given a sorted (in descending order) list of numbers and a number to find in the list,
# write a function which finds the number within minimum number of steps
# input = list of numbers and number to be found
# output = position of the number in the list, if number present in the list otherwise None
# constraint: the function should find the given in minimum number of steps

def binarysearch(cards, query, left, right):
    if right - left <= 0:
        return None
    mid = (right + left) // 2
    if cards[mid] == query:
        return mid

    if cards[mid] > query:
        return binarysearch(cards, query, mid + 1, right)
    else:
        return binarysearch(cards, query, left, mid)


def locate_card(cards, query):
    left = 0
    right = len(cards)
    result = binarysearch(cards, query, left, right)
    if result is None:
        print("Number not in the list!")
    else:
        print("Number found at position: ", result)

if __name__ == '__main__':
    li = [34,23,20,18,16,13,12,9,7,6,6,5,2,1]
    locate_card(li,23)
    locate_card(li,4)
    locate_card(li,6)
    locate_card(li,9)

    newli = []
    for i in range(1000000,0,-1):
        newli.append(i)

    locate_card(newli,24876)
    locate_card(newli,0)
    locate_card(newli,8888)
    locate_card(newli,1)
    locate_card(newli,-1)