# Given arrival and departure times of all trains that reach a railway station.
# Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day.
# Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other.
# At any given instance of time, same platform can not be used for both departure of a train and arrival of another train.
# In such cases, we need different platforms.


# Function to find the minimum number of platforms required at the
# railway station such that no train waits.

def search(nums,target):
    numcount = 0
    for i in nums:
        if i < target:
            numcount = numcount + 1
    return numcount


def minimumPlatform(n, arr, dep):
    max_count = 0
    arr_count = 0
    arr.sort()
    dep.sort()
    for i in range(n):
        arr_count = arr_count + 1
        num_departed = search(dep[:i],arr[i])
        if num_departed > 0:
            arr_count = arr_count - num_departed
            for i in range(num_departed):
                dep.pop(0)
        if max_count < arr_count:
            max_count = arr_count
    return max_count

if __name__ == '__main__':
    n = 6
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minimumPlatform(n,arr,dep))
    n = 3
    arr = [900, 1100, 1235]
    dep = [1000, 1200, 1240]
    print(minimumPlatform(n, arr, dep))