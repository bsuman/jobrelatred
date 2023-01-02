# Reverse bits of a given 32 bits unsigned integer.


def reverseBits(n: int) -> int:
    sbin = '{0:b}'.format(n)
    ln = len(sbin)
    for i in range(32-ln):
        sbin = '0' + sbin
    newint = int(sbin[::-1], 2)
    return newint


if __name__ == '__main__':
    print(reverseBits(43261596))
