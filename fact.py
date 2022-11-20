# function to generate the factorial of n
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


# function generate the mutliplication
def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


# function to implement fibonacci series
def fibonacci(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fibonacci(m - 1) + fibonacci(m - 2)


if __name__ == '__main__':
    print(factorial(3))
    print(multiply(2,4))
    print(fibonacci(4))