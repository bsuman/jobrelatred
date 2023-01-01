# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

def isPowerOfTwo(n: int):
    if n == 2:
        return True
    elif n == 1:
        return True
    elif n % 2 != 0:
        return False
    return isPowerOfTwo(n // 2)


if __name__ == '__main__':
    print(isPowerOfTwo(1))
    print(isPowerOfTwo(16))
    print(isPowerOfTwo(62))
    print(isPowerOfTwo(3))