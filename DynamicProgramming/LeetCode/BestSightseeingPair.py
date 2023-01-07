# You are given an integer array values where values[i] represents the value of the ith sightseeing spot.
# Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

def maxScoreSightseeingPair(values: list[int]) -> int:
    ln = len(values)
    maxval = 0
    val = 0
    for i in range(ln):
        maxval = max(maxval, values[i] + val)
        val = max(val,values[i])-1
    return maxval


if __name__ == '__main__':
    values = [8, 1, 5, 2, 6]
    print(maxScoreSightseeingPair(values))
    values = [1, 2]
    print(maxScoreSightseeingPair(values))
