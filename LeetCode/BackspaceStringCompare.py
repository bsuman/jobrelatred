# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

def backspaceCompare(s: str, t: str) -> bool:
        

if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print(backspaceCompare(s,t))
    s = "ab##"
    t = "c#d#"
    print(backspaceCompare(s, t))