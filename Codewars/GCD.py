# algorithm to implement GCD of two number m and n
def GCD(m, n):
    if m >= n and m % n == 0:
        return n
    elif n >= m and n % m == 0:
        return m
    else:
        numbers = range(min(m, n) - 1, 0, -1)
        for i in numbers:
            if i > 0 and m % i == 0 and n % i == 0:
                return i


if __name__ == '__main__':
    ix = GCD(12, 4)
    print("GCD:", ix)
    ix = GCD(4, 12)
    print("GCD:", ix)
    ix = GCD(6, 6)
    print("GCD:", ix)
    ix = GCD(100, 30)
    print("GCD:", ix)
