# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s: str, t: str) -> bool:
    lsub = len(s)
    if lsub == 0:
        return True
    elif lsub > len(t):
        return False

    isFound = False
    j = 0
    for i in range(lsub):
        isFound = False
        while j < len(t):
            if s[i] == t[j]:
                isFound = True
                j = j+1
                break
            j = j + 1
        if not isFound:
            return False
    return isFound


if __name__ == '__main__':
    s = "aaaaaa"
    t = "bbaaaa"
    print(isSubsequence(s,t))
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s,t))
