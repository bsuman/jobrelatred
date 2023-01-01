# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


def hammingWeight(n: int) -> int:
    li =bin(n)
    num_ones = li.count('1')
    return num_ones


if __name__ == '__main__':
    print(hammingWeight(11))
    print(hammingWeight(128))
    print(hammingWeight(4294967293))