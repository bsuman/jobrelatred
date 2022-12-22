# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber.
# We followed him to a secret warehouse, where we assume to find all the stolen stuff.
# The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
#
# The keypad has the following layout:
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally).
# E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm.
# That's why we can try out all possible (*) variations.
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
# Can you help us find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits.
# We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's.
# We already prepared some test cases for you.
# Detective, we are counting on you!

keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['x', '0', 'x']]


def getposition(num):
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == num:
                return i, j
    return -1, -1


def getneighbors(i, j):
    neighbours = []
    if i == -1 or j == -1:
        return neighbours
    neighbours.append(keypad[i][j])
    if i - 1 >= 0 and keypad[i - 1][j] != 'x':
        neighbours.append(keypad[i - 1][j])
    if i + 1 < 3 and keypad[i + 1][j] != 'x':
        neighbours.append(keypad[i + 1][j])
    if j - 1 >= 0 and keypad[i][j - 1] != 'x':
        neighbours.append(keypad[i][j - 1])
    if j + 1 < 3 and keypad[i][j + 1] != 'x':
        neighbours.append(keypad[i][j + 1])
    return neighbours


def getpossiblekeys(num):
    i, k = getposition(num)
    return getneighbors(i, k)


def getcombinations(combinations, listofnb, pos):
    numKeys = len(combinations)
    nstr = ""
    rstr = ""
    for nk in range(numKeys):
        rstr = combinations[nk]
        for ng in listofnb:
            if pos == 0:
                nstr = ng + rstr[pos + 1:len(rstr)]
            elif pos + 1 == len(rstr):
                nstr = rstr[:pos] + ng
            else:
                nstr = rstr[:pos] + ng + rstr[pos + 1:len(rstr)]
            if combinations.count(nstr) <= 0:
                combinations.append(nstr)


def get_pins(observed):
    # keypad store as matrix
    istr = str(observed)
    combinations = []
    combinations.append(istr)
    strlen = len(istr)
    for pos in range(strlen):
        listofnb = getpossiblekeys(istr[pos])
        getcombinations(combinations, listofnb, pos)
    return combinations

if __name__ == '__main__':
    #combinations = get_pins(11)
    #print(combinations)
    #combinations.clear()
    combinations = get_pins(369)
    print(combinations)
