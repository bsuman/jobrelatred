# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.insert(0, ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if len(stack) > 0:
                if ch == ')' and stack.pop(0) != '(':
                    return False
                elif ch == '}' and stack.pop(0) != '{':
                    return False
                elif ch == ']' and stack.pop(0) != '[':
                    return False
            else:
                return False

    if len(stack) > 0:
        return False
    return True


if __name__ == "__main__":
    print(isValid(""))