# Complete the function/method (depending on the language) to return true/True
# when its argument is an array that has the same nesting structures and same
# corresponding length of nested arrays as the first array.
#
# For example:
#
# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

def checkstructure(original, other):
    if type(original) == list and type(other) != list:
        return False
    elif type(original) != list and type(other) == list:
        return False
    elif type(original) != list and type(other) != list:
        return True
    else:
        if len(original) != len(other):
            return False  # if the len of the inputs don't match
        for i in range(len(original)):
            if checkstructure(original[i], other[i]) == False:
                return False
            else:
                continue
        return True

def same_structure_as(original, other):
    print("Original:", str(original))
    print("Other:", str(other))

    return checkstructure(original, other)


if __name__ == '__main__':
    #if same_structure_as([1, [1, 1]], [2, [2, 2]]):
    #if same_structure_as([1, '[', ']'], ['[', ']', 1]):
    if same_structure_as([1,[1,1]],[2,[2]]):
        print("Same Structure!")
    else:
        print("Not same structure!")