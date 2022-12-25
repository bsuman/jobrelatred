# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    mlsubstr = 0
    limit = len(s)
    index = 0
    while index < limit:
        startindex = index
        clsubstr = 0
        alreadyseen = []
        while startindex < limit:
            if s[startindex] in alreadyseen:
                alreadyseen = []
                break
            else:
                alreadyseen.append(s[startindex])
                clsubstr = clsubstr + 1
            startindex = startindex + 1

        if mlsubstr < clsubstr:
            mlsubstr = clsubstr
        index = index + 1
    return mlsubstr


if __name__ == '__main__':
    s =" "
    print(lengthOfLongestSubstring(s))
    s = "dvdf"
    print(lengthOfLongestSubstring(s))
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))