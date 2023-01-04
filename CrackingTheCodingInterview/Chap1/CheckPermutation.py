# Given two strings, write a method to decide if one is a permutation of the other.

def isPermutation(istr1, istr2):
    # strings which are permutations of each other should have same length
    if len(istr1) != len(istr2):
        return False
    # assuming strings are ASCII english characters
    # initialize all character count to 0
    character_count = [0] * 128

    for i in istr1:
        # for each character in string 1 increment the character count
        character_count[ord(i)] += 1

    for i in istr2:
        # for each character in string 1 decrement the character count
        character_count[ord(i)] -= 1
        # character count is less than 0
        # if the decrement was done for character not present in the string 1
        # or if the count of character i do not match in both strings
        if character_count[ord(i)] < 0:
            return False

    return True


if __name__ == '__main__':
    print(isPermutation('dog','god'))
    print(isPermutation('dog', 'good'))
    print(isPermutation('dog', 'cod'))
    print(isPermutation('aaabbb', 'bbaaba'))
    print(isPermutation('aaabbb', 'bbabba'))