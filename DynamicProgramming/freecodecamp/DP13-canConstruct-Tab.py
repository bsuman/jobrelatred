# write a function canConstruct(targetStr,wordbank) that accetps a target string and an array of strings
# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the workbank array
# constraints: elements of the word bank can be used as many times as needed
# use tabulation for optimization

def canConstruct(targetStr,wordbank):
    limit = len(targetStr)+ 1
    l = [False for i in range(limit)]
    l[0] = True
    for i in range(0, limit):
        if l[i] == True:
            for j in wordbank:
                index = targetStr[i:].find(j)
                if index == 0:
                    l[i+len(j)] = True

    return l[len(targetStr)]


if __name__ == '__main__':

    print(canConstruct('abcdef', ['ab', 'abc', 'ef', 'def', 'abcd']))
    print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))