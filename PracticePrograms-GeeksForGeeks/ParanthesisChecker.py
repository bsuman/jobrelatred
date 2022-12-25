# Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.


def ispar(x):
    stack = []
    for i in x:
        if i == '(' or i == '{' or i == '[':
            stack.insert(0, i)
        else:
            if i == ')' and (len(stack) == 0 or stack.pop(0) != '('):
                return False
            elif i == '}' and (len(stack) == 0 or stack.pop(0) != '{'):
                return False
            elif i == ']' and (len(stack) == 0 or stack.pop(0) != '['):
                return False

    if len(stack) > 0:
        return False
    return True


if __name__ == '__main__':
    s = '{([])}'
    print(ispar(s))
    s = '()'
    print(ispar(s))
    s = '([]'
    print(ispar(s))
