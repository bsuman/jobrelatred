# write a function countConstruct(target,wordBank) that accepts a target string and an array of strings
# return number of ways target can be made using the words of the wordbank
# constraint: the words in the wordbank can be used unlimited number of times
# use tabulation for optimization

def countConstruct(target,wordBank):
    limit = len(target) +1
    table = [0 for i in range(limit)]
    table[0] = 1

    for i in range(0,limit):
        if table[i]:
            for j in wordBank:
                if j == target[i:i+len(j)]:
                    table[i+len(j)] = table[i] + table[i+len(j)]

    print(table)
    return table[len(target)]


if __name__ == '__main__':
    print(countConstruct('abcdef', ['ab', 'abc', 'ef', 'def', 'abcd']))
    print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))