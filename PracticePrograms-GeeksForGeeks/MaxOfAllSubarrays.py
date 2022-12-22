# Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

def max_of_subarrays(arr, n, k):
    subarr = []
    for i in range(n + 1 - k):
        subarr.append(max(arr[i:i + k]))
    return subarr

if __name__ == '__main__':
    N = 9
    K = 3
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    print(max_of_subarray(arr, N, K))
