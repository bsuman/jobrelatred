def zero_plentiful(arr):
    count = 0
    retval = 0
    print(arr)
    l = len(arr)
    i = 0
    while i < l:
        if arr[i] == 0:
            count = count + 1
        elif arr[i] != 0 and (0 < count < 4):
            return 0
        if count >= 4 and (arr[i] != 0 or i==l-1):
            retval = retval + 1
            count = 0

        i = i + 1
    return retval



if __name__ == '__main__':
    res = zero_plentiful([0, 0, 0, 0, 2, 0, 0, 0, 0, 0, -12, 0, 0, 0, 0] )
    print(res)