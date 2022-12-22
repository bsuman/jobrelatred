# implement merge sort
# recursively do the following steps
# split the list in 2 halves
# sort of each half
# merge




def mergesort(n):
    if len(n) <= 1:
        return n
    l = mergesort(n[0:len(n) // 2])
    r = mergesort(n[len(n) // 2:])
    return (merge(l,r))

def merge(l1,l2):
    l3 = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l3.append(l1.pop(0))

        elif l1[0] > l2[0]:
            l3.append(l2.pop(0))

        elif l1[0] == l2[0]:
            l3.append(l2.pop(0))
            l1.pop(0)

    while len(l1) > 0:
        l3.append(l1.pop(0))

    while len(l2) > 0:
        l3.append(l2.pop(0))


    return l3

def listdiff(l1,l2):
    l3 = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l3.append(l1.pop(0))

        elif l1[0] > l2[0]:
            l3.append(l2.pop(0))

        elif l1[0] == l2[0]:
            l1.pop(0)
            l2.pop(0)

    while len(l1) > 0:
        l3.append(l1.pop(0))

    while len(l2) > 0:
        l3.append(l2.pop(0))

    return l3

if __name__ == '__main__':
    print(listdiff([1,2,3,6],[2,4,6,8]))