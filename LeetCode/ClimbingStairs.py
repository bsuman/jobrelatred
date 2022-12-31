# You are climbing a staircase.
# It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


def climbStairs(n, l={}):
    # if it takes 0 step to reach the top, then there is no way of doing it as one is allowed only 1 or 2 steps at a time
    if n in l.keys():
        return l[n]
    elif n == 1:
        return 1
    # if it takes 1 step to reach the top, then there is one way of doing.
    elif n == 2:
        return 2
    else:
        l[n] = climbStairs(n - 1, l) + climbStairs(n - 2, l)
        return l[n]


if __name__ == '__main__':
    n = 3
    print(climbStairs(n))
    n = 2
    print(climbStairs(n))
    n = 4
    print(climbStairs(n))
    n = 35
    print(climbStairs(n))
