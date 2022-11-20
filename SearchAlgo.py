# This exercise includes all the searching algorithms
# Goal: Learn about the standard search algorithm and their efficiency
# To learn about the efficiency all search algorithms are implemented with the same data structure

# LINEAR SEARCH
# BINARY SEARCH
# 

def binarysearch(sq, l, r, elem):
    # check if the sq is empty
    if r - l == 0:
        return False
    # calculate mid
    mid = (r + l ) // 2
    if sq[mid] == elem:
        return True
    elif sq[mid] > elem:
        return binarysearch(sq, l, mid, elem)
    else:
        return binarysearch(sq, mid + 1, r, elem)


if __name__ == '__main__':
    sq = [23,34,56,7,8,9,12]
    elem = 9
    l = 0
    r = len(sq) - 1
    sq.sort()
    if binarysearch(sq,l,r,elem):
        print("Element Found !!")
    else:
        print("Element does not exist in the sequence")
