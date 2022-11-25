# write a function canConstruct(targetStr,wordbank) that accetps a target string and an array of strings
# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the workbank array
# constraints: elements of the word bank can be used as many times as needed

def canConstruct(targetStr, wordbank,d= {}):
    if len(targetStr) == 0:
        return True
    elif targetStr in d.keys():
        return d[targetStr]
    for i in wordbank:
        index = targetStr.find(i)
        if index == 0:
            remainder = targetStr[len(i):len(targetStr)]
            if canConstruct(remainder, wordbank,d):
                d[targetStr] = True
                return d[targetStr]

    d[targetStr] = False
    return False


if __name__ == '__main__':

    print(canConstruct('abcdef', ['ab', 'abc', 'ef', 'def', 'abcd']))
    print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))