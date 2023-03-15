# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
def getcleanstring(s):
    sl = []
    for letter in s:
        if letter != '#':
            sl.insert(0, letter)
        else:
            if len(sl) > 0:
                sl.pop(0)

    return str(sl)
def backspaceCompare(s: str, t: str) -> bool:
        ns = getcleanstring(s)
        nt = getcleanstring(t)
        s.find()
        return ns==nt


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print(backspaceCompare(s,t))
    s = "ab##"
    t = "c#d#"
    print(backspaceCompare(s, t))