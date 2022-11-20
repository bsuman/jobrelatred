# implement selection sort
# scan the list and find the position of the smallest element
# swap with the first element in the list
# continue until the list is sorted


def selectionsort(sq):
    for start in range(len(sq)):
        minpos = start
        for i in range(start, len(sq)):
            if sq[i] < sq[minpos]:
                minpos = i
        sq[start], sq[minpos] = sq[minpos], sq[start]
    return sq



if __name__ == '__main__':
    print(selectionsort([23,11,2,45,21]))