# function to calculate the nth entry of fibonacci series

def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib(n, l={}):
    if n in l.keys():
        return l[n]
    elif n <= 2:
        return 1
    else:
        l[n] = fib(n - 1,l) + fib(n - 2,l)
        return l[n]



if __name__ == '__main__':
    print(fib(7))
    print(fib(50))