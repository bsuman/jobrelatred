# write a function allConstruct(target,wordBank) that accepts a target string and an array of strings
# returns 2D array with all the ways that the target can be constructed by concatenating elements of the wordbank
# each entry of the 2D list will be the combination of the words in the wordbank together forming the target
# constraint: the words in the wordbank can be used unlimited number of times
# use tabulation to optimize solution


def allConstruct(target,wordBank):
    limit = len(target)
    table = [None for i in range(limit + 1)]
    table[0] =[[]]
    for i in range(limit+1):
        if table[i] is not None:
            for j in wordBank:
                index = i+len(j)
                if j == target[i:index]:
                    for k in table[i]:
                        new = k + [j]
                        if table[index] is not None:
                            table[index] = table[index] + [new]
                        else:
                            table[index] = [new]
    return table[limit]

if __name__ == '__main__':
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd','ef','c']))
    print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))