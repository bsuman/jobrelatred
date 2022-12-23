# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s: str) -> str:
    wordlist = s.split(' ')
    fstr = ''
    wl = len(wordlist)
    for i in range(wl):
        word = wordlist[i]
        fstr = fstr + word[::-1]
        if i < wl-1 and wl > 1:
            fstr = fstr + ' '
    return fstr


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    rs = reverseWords(s)
    print(rs)