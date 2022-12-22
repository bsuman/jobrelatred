# Given an unsorted array A of size N that contains only non-negative integers,
# find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.
# In case of multiple sub-arrays, return the subarray indexes which comes first on moving from left to right.
# Note:- Both the indexes in the array should be according to 1-based indexing.
# You have to return an arraylist consisting of two elements left and right.
# In case no such subarray exists return an array consisting of element -1.


def subarraySum(arr, N, S):
    arraylist = []
    if N == 0 or S < 0:
        return arraylist.append(-1)

    for i in range(N):
        j = i
        remain = S
        while j < N:
            if arr[j] <= remain:
                remain = remain - arr[j]
                if remain == 0:
                    arraylist.append(i + 1)
                    arraylist.append(j + 1)
                    return arraylist
                else:
                    j = j + 1
            else:
                break

    return arraylist.append(-1)


if __name__ == '__main__':
    A = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183,
         22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    N = 42
    S = 468
    print(subarraySum(A, N, S))

    N = 5
    S = 12
    A = [1, 2, 3, 7, 5]
    print(subarraySum(A, N, S))
    N = 10
    S = 15
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(subarraySum(A, N, S))
