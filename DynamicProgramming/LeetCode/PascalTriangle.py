# Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
def generate(numRows) -> list[list[int]]:
    dp = []
    for i in range(1, numRows + 1):
        if i == 1:
            dp.append([1])
        elif i == 2:
            dp.append([1, 1])
        else:
            numlist = dp[i - 2]
            tmp = [1]
            nln = len(numlist)
            for j in range(nln):
                if j + 1 < nln:
                    num = numlist[j] + numlist[j + 1]
                else:
                    num = numlist[j]
                tmp.append(num)
            dp.append(tmp)
    return dp


if __name__ == '__main__':
    print(generate(6))
