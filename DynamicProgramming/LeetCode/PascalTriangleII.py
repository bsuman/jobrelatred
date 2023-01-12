# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

def getRow(rowIndex) -> list[int]:
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    numlist = [1, 1]
    current = None
    for i in range(2, rowIndex+1):
        current = [1]
        nln = len(numlist)
        for j in range(nln):
            if j + 1 < nln:
                num = numlist[j] + numlist[j + 1]
            else:
                num = numlist[j]
            current.append(num)
        numlist = current
    return current


if __name__ == '__main__':
    print(getRow(3))
