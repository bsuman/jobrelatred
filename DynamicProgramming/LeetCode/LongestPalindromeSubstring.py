# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s: str) -> str:
    rlen = 0
    rstr = ''
    ls = len(s)
    for ch in range(ls):
        left = ch
        right = ch
        while left >= 0 and right < ls and s[left] == s[right]:
            l = right - left + 1
            if rlen < l:
                rlen = l
                rstr = s[left:right + 1]
            left -= 1
            right += 1

        left = ch
        right = ch + 1
        while left >= 0 and right < ls and s[left] == s[right]:
            l = right - left + 1
            if rlen < l:
                rlen = l
                rstr = s[left:right + 1]
            left -= 1
            right += 1
    return rstr


if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))