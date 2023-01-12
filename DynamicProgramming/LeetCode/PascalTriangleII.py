# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

def getRow(rowIndex) -> list[int]:
    dp = []
    for i in range(0, rowIndex+1):
        if i == 0:
            dp.append([1])
        elif i == 1:
            dp.append([1, 1])
        else:
            numlist = dp[i - 1]
            tmp = [1]
            nln = len(numlist)
            for j in range(nln):
                if j + 1 < nln:
                    num = numlist[j] + numlist[j + 1]
                else:
                    num = numlist[j]
                tmp.append(num)
            dp.append(tmp)
    return dp[rowIndex]


if __name__ == '__main__':
    print(getRow(3))
