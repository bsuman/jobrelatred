# implementation of the quicksort algorithm with first element used as the pivot


def quicksort(list1, left, right):
    if right - left <= 1:
        return ()

    yellow = left + 1

    for green in range(left + 1, right):
        if list1[green] <= list1[left]:
            list1[yellow], list1[green] = list1[green], list1[yellow]
            yellow = yellow + 1

    list1[left], list1[yellow -1] = list1[yellow-1], list1[left]
    quicksort(list1, left, yellow - 1)
    quicksort(list1, yellow, right)


if __name__ == '__main__':
    list1 = [43, 2, 4, 78, 29, 82, 13]
    quicksort(list1, 0, len(list1))
    print(list1)
