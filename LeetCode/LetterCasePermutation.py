# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.


def letterCasePermutation(s: str):
    flist = [s]
    queue = [s]
    while len(queue)>0:
        sstr = queue.pop()
        for i in range(len(sstr)):
            if not sstr[i].isdigit():
                tmp = sstr[:i] + sstr[i].swapcase() + sstr[i+1:]
                if tmp not in flist:
                    flist.append(tmp)
                    queue.append(tmp)

    return flist


if __name__ == '__main__':
    s = "Jw"
    print(letterCasePermutation(s))
    s = "a1b2"
    print(letterCasePermutation(s))
    s = "3z4"
    print(letterCasePermutation(s))
    s = "Su1Ma2N"
    print(letterCasePermutation(s))
    s = "123"
    print(letterCasePermutation(s))