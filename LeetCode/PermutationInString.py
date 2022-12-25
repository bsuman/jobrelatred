# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

def checkInclusion(s1: str, s2: str):
    limit1 = len(s1)
    limit2 = len(s2)
    if len(s2) < len(s1):
        return False
    elif s1 == s2:
        return True

    for index in range(limit2):
        if s2[index] in s1:
            matching = 0
            for j in range(limit1):
                if s1[j] not in s2[index:(index + limit1)] or s1.count(s1[j]) != s2[index:(index + limit1)].count(
                        s1[j]):
                    break
                else:
                    matching = matching + 1
            if matching == limit1:
                return True
    return False


if __name__ == '__main__':
    s1 = "ab"
    s3 = "eidbaoo"
    print(checkInclusion(s1, s3))
    s2 = "eidaabooo"
    print(checkInclusion(s1, s2))
    s1 = "hello"
    s2 = "ooolleoooleh"
    print(checkInclusion(s1, s2))
    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2))
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    print(checkInclusion(s1, s2))
