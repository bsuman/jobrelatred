# write a function countConstruct(target,wordBank) that accepts a target string and an array of strings
# return number of ways target can be made using the words of the wordbank
# constraint: the words in the wordbank can be used unlimited number of times


def countConstruct(target, wordBank,d = {}):
    if len(target) == 0:
        return 1
    elif target in d.keys():
        return d[target]

    numways = 0
    for i in wordBank:
        index = target.find(i)
        if index == 0:
            result = countConstruct(target[len(i):], wordBank,d)
            numways = result + numways
            d[target]= numways

    return numways


if __name__ == '__main__':
    d = {}
    print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))