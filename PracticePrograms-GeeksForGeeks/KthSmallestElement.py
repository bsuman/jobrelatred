# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(log(n))
# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 105
# 1 <= K <= N

def kthSmallest(arr, l, r, k):
    arr.sort()
    return arr[k-1]


if __name__ == '__main__':
    N = 5
    arr = [7,10,4,20,15]
    K = 4
    print(kthSmallest(arr,0, N-1,K))

    N = 6
    arr = [7,10,4,3,20,15]
    K = 3
    print(kthSmallest(arr, 0, N - 1, K))