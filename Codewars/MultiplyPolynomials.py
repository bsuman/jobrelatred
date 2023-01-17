# Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.
# For example, the lists [2, 0, 5, 7] and [3, 4, 2] represent the polynomials  2+5𝑥2+7𝑥3  and  3+4𝑥+2𝑥2 .
#
# Their product is
#
# (2×3)+(2×4+0×3)𝑥+(2×2+3×5+4×0)𝑥2+(7×3+5×4+0×2)𝑥3+(7×4+5×2)𝑥4+(7×2)𝑥5  i.e.
#
# 6+8𝑥+19𝑥2+41𝑥3+38𝑥4+14𝑥5
# It can be represented by the list [6, 8, 19, 41, 38, 14].


def multiply(poly1, poly2):
    lp1 = len(poly1)
    lp2 = len(poly2)
    if lp1 == 0:
        return poly2
    elif lp2 == 0:
        return poly1

    fl = lp1 + lp2 - 1
    flist = [0] * fl
    index = 0
    while index < fl:
        for i in range(lp1):
            for j in range(lp2):
                if index == (i + j):
                    num1 = poly1[i]
                    num2 = poly2[j]
                    tmp = num1 * num2
                    flist[index] = flist[index] + (tmp)
        index = index + 1
    return flist


if __name__ == '__main__':
    poly1 = [12, 2, 4, 5]
    poly2 = [2, 8]
    flist = multiply(poly1, poly2)
    print(flist)
