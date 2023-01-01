# write a function allConstruct(target,wordBank) that accepts a target string and an array of strings
# returns 2D array with all the ways that the target can be constructed by concatenating elements of the wordbank
# each entry of the 2D list will be the combination of the words in the wordbank together forming the target
# constraint: the words in the wordbank can be used unlimited number of times



def allConstruct(target, wordBank):
    if len(target) == 0:
        return [[]]
    combi = []
    for i in wordBank:
        result = [[]]
        if target.find(i) == 0:
            remainder = target[len(i):len(target)]
            result = allConstruct(remainder, wordBank)
            for list1 in result:
                list1.insert(0, i)
            combi = combi + result

    return combi


if __name__ == '__main__':
    print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))