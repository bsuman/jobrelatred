# Buddy pairs
# You know what divisors of a number are.
# The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself.
# In the following description, divisors will mean proper divisors.
# For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.
#
# Let s(n) be the sum of these proper divisors of n.
# Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:
#
# (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1
#
# For example 48 & 75 is such a pair:
#
# Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
# Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
# Task
# Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs
# such that n (positive integer) is between start (inclusive) and limit (inclusive);
# m can be greater than limit and has to be greater than n
#
# If there is no buddy pair satisfying the conditions, then return "Nothing"
#
# Examples
# buddy(10, 50) returns [48, 75]
# buddy(48, 50) returns [48, 75]
import math


import math
def getsumdivisors(num, sumlim):
    sum = 0
    lim = int(math.sqrt(num))
    i = 1
    while i <= lim:
        if num % i == 0:
            div = num // i
            sum = sum + i
            if sumlim > 0 and sum > sumlim:
                return -1
            if div != num and div != i:
                sum = sum + div
                if sumlim > 0 and sum > sumlim:
                    return -1
        i = i + 1
    return sum


def buddy(start, limit):
    if start < 0 or limit <= 0:
        return "Nothing"
    for n in range(start, limit + 1, 1):
        n_sum = getsumdivisors(n, 0)
        m = n_sum - 1
        m_sum = getsumdivisors(m, n + 1)
        if m_sum > -1 and m_sum == n + 1 and m > n:
            return [n, m]

    return "Nothing"

if __name__ == '__main__':
    print(buddy(10, 50))  # [48, 75]
    print(buddy(2177, 4357))  # "Nothing"
    print(buddy(57345, 90061))  # [62744, 75495]
    print(buddy(1071625, 1103735))  # [1081184, 1331967]
    print(buddy(310,2755))  # [1050, 1925]