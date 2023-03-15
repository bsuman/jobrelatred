import itertools


def get_shortest_unique_substring(arr, str):
    permutations = list(itertools.permutations(arr))
    print(permutations)
    for permutation in permutations:
        allletterspresent = True
        for letter in str(permutation):
            if str.find(letter) == -1:
                allletterspresent = False
                break;
        if allletterspresent:
            return permutation

    return ""

if __name__ == '__main__':
    print(get_shortest_unique_substring(["A"], "A"))