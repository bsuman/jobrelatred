# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# assuming that case sensitivity does not matter
def isUnique(istr) -> bool:
    seen_alpha = {}
    for i in istr.lower():
        if i in seen_alpha.keys():
            return False
        else:
            seen_alpha[i] = True
    return True


# assuming english language
# assuming not unicode but ASCII character set
def isUnique2(istr) -> bool:
    # only 128 unique characters present english language
    if len(istr) > 128:
        return False
    charpresent = [False] * 128
    for i in istr:
        if charpresent[ord(i)]:
            return False
        else:
            charpresent[ord(i)] = True
    return True


if __name__ == '__main__':
    print(isUnique2('Suman'))
    print(isUnique2('Ana'))
    print(isUnique2('ana'))
