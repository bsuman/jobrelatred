# The Tribonacci sequence Tn is defined as follows:
# T0 = 0
# T1 = 1
# T2 = 1
# Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

def Tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    num_list = [None]*(n+1)
    num_list[0] = 0
    num_list[1] = 1
    num_list[2] = 1
    for i in range(3, n+1):
        num_list[i] = num_list[i-3] + num_list[i-2] + num_list[i-1]

    return num_list[n]


if __name__ == '__main__':
    print(Tribonacci(4))
    print(Tribonacci(25))