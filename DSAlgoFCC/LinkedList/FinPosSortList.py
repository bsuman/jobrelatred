# QUESTION 1: Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# Problem Definition: Given a sorted (in descending order) list of numbers and a number to find in the list,
# write a function which finds the number within minimum number of steps
# input = list of numbers and number to be found
# output = position of the number in the list, if number present in the list otherwise None
# constraint: the function should find the given in minimum number of steps

def binarysearch(cards, query, left, right, foundposition):
    if right - left <= 0:
        return foundposition
    mid = (right + left) // 2
    if cards[mid] == query:
        if foundposition == -1 or mid < foundposition:
            foundposition = mid
            if cards[mid - 1] < query:
                return foundposition

    if cards[mid] > query:
        return binarysearch(cards, query, mid + 1, right, foundposition)
    else:
        return binarysearch(cards, query, left, mid, foundposition)


def locate_card(cards, query):
    left = 0
    right = len(cards)
    foundposition = -1
    result = binarysearch(cards, query, left, right, foundposition)
    if result == -1:
        print("Number not in the list!")
    else:
        print("Number " + str(query) + " found at position:", result)


if __name__ == '__main__':
    li = [5,4,3,2,1,0]
    locate_card(li, 0)


    li = [34, 23, 20, 18, 16, 6, 6, 6, 5, 4, 3, 2, 1]
    locate_card(li, 23)
    locate_card(li, 4)
    locate_card(li, 6)
    newli = []
    locate_card(newli, 6)
    for i in range(1000000, 0, -1):
        newli.append(i)

    newli[999993] = 6
    newli[999995] = 6
    newli[999996] = 6
    locate_card(newli, 6)
