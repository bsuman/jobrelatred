import math


def reverse_num(x: int) -> int:
    s_x = str(abs(x))
    s_x = s_x[::-1]
    MAX = math.pow(2, 31) - 1
    MIN = math.pow(-2, 31)
    num = int(s_x)

    if num>MAX or num< MIN:
        return 0
    else:
        if x > 0:
            return num
        else:
            return -num



if __name__ == '__main__':
    print(reverse_num(-123))
