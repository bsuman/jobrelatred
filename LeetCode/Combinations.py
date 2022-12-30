# Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

def combine(n: int, k: int):
    flist = []
    limit = n - k + 1
    queue = []
    for i in range(1, limit + 1):
        queue.append([i])

    while len(queue) > 0:
        numlist = queue.pop(0)
        if len(numlist) == k:
            flist.append(numlist)
        else:
            ln = len(numlist)
            startindex = numlist[ln - 1] + 1
            for i in range(startindex, n + 1):
                if i <= (n + 1) - (k - ln):
                    tmp = numlist + [i]
                    queue.append(tmp)
    return flist


if __name__ == '__main__':
    # print(combine(1, 1))
    # print(combine(2, 1))
    print(combine(4, 3))
    print(combine(5, 3))
