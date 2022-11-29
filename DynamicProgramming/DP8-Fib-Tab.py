# function to calculate the nth entry of fibonacci series
# optimize using the tabulation method ( converting the recursive solution to iterative)

def fib(n):
    l = [0 for i in range(n + 1)]
    if n >=0:
        l[1] = 1

    i = 0
    while i + 2 <= n:
        l[i+2] = l[i+1] + l[i] # fib(n-2) + fib(n-1) = f(n)
        i = i + 1

    if i + 1 == n:
        l[i + 1] = l[i] + l[i-1]

    return l[n]

if __name__ == '__main__':
    print(fib(7))
    print(fib(8))
    print(fib(6))
    print(fib(50))