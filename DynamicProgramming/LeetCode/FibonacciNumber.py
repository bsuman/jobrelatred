# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1
# Given n, calculate F(n).

def fib(n: int) -> int:
    fib_nums = [None]*(n+1)
    fib_nums[0] = 0
    fib_nums[1] = 1
    for i in range(2,n+1):
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]

    return fib_nums[n]

if __name__ == '__main__':
    print(fib(2))
    print(fib(3))
    print(fib(4))