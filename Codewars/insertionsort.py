# implementation of insertion sort algorithm
# create a new list start with the first element of the input list
# check if the next element in the input list is smaller than topmost element in the new list
# if yes, then put the next element to the left of the list
# if not, then put the next element to the right of the list

def insertionsort(sq):
    for i in range(len(sq)):
        pos = i
        while pos > 0 and sq[pos] < sq[pos - 1]:
            sq[pos], sq[pos - 1] = sq[pos - 1], sq[pos]
            pos = pos - 1


if __name__ == '__main__':
    nl = [23, 11, 2, 45, 21]
    insertionsort(nl)
    print(nl)
