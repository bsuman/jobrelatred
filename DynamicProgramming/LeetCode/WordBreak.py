# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def checkstring(substring, wordDict, computed):
    if len(substring) == 0:
        return True
    elif substring in computed.keys():
        return computed[substring]

    for word in wordDict:
        index = substring.find(word)
        if index == 0:
            remainder = substring[index + len(word):]
            if checkstring(remainder, wordDict, computed):
                computed[substring] = True
                return computed[substring]
    return False


def wordBreak_recur(s, wordDict) -> bool:
    computed = {}
    return checkstring(s, wordDict, computed)


def wordBreak(s, wordDict) -> bool:
    ln = len(s)
    dp = [False] * (ln+1)
    # always possible to form an empty string
    dp[0] = True
    for i in range(0,ln):
        if dp[i]:
            for word in wordDict:
                index = s[i:].find(word)
                if index == 0 and i + len(word) <= ln:
                    dp[i + len(word)] = True
    return dp[ln]


if __name__ == '__main__':
    print(wordBreak("leetcode", ["leet", "code"]))
