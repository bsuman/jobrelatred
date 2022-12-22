import math


# wrong answer for n = 43
def numSquares(n: int) -> int:
    min_count = 0
    limit = int(math.sqrt(n))

    for i in range(limit, 0, -1):
        start = i
        count = 0
        remainder = n
        while start > 0:
            while start * start <= remainder:
                remainder = remainder - start * start
                count = count + 1
                if remainder == 0:
                    break
            start = start - 1
        if min_count == 0:
            min_count = count
        elif min_count > count:
            min_count = count

    return min_count


if __name__ == '__main__':
    n = 43
    print(numSquares(n))
