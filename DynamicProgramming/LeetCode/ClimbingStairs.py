# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    numsteps = [None] * (n + 1)
    if n == 1:
        return 1

    numsteps[0] = 0
    numsteps[1] = 1
    numsteps[2] = 2
    for i in range(3, n + 1):
        numsteps[i] = numsteps[i - 1] + numsteps[i - 2]

    return numsteps[n]


if __name__ == '__main__':
    print(climbStairs(2))
    print(climbStairs(4))
    print(climbStairs(3))