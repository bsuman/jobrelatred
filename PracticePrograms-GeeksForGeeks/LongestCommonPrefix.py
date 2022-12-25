# Given a array of N strings, find the longest common prefix among all strings present in the array.

def longestCommonPrefix(arr, n):
    len_min = 0
    len_min_index = 0
    for i in range(n):
        if i == 0 or len_min > len(arr[i]):
            len_min = len(arr[i])
            len_min_index = i

    end = len_min
    minstring = arr[len_min_index]
    while end > 0:
        found = 0
        sstr = minstring[:end]
        for i in range(n):
            if i != len_min_index:
                foundat = arr[i].find(sstr)
                if foundat == -1 or foundat!= 0:
                    break
                else:
                    found = found + 1
        if found == (n - 1):
            return minstring[:end]
        end = end - 1
    return '-1'


if __name__ == '__main__':
    N = 4
    arr = ['dmlrpjyatcoqotxzplqmlptaipczhlikztcofaoaedruyqundkzqatqkkvjrgucineyugnxmsohsgdfmngcpbvamqldyfhgvnfrv', 'oioerglunzjvbzxwblooqnuytrnyijuxtibkoogdppzrqyptjeizrezmvnnfyherqidgyjkoyjfrhwkscsrvytivivbgcfxupab', 'llclwjcdfpvijodijndriexnmwhbyiplvtxrcbwkqtsaixitn','lvskkgjujheztaustxtqhklbkvyupnhajbmvhvprfusawmspjlhsvtthouddhlfsmsqwpfpubhuzvmrhaazx']
    str1 = longestCommonPrefix(arr, N)
    print(str1)
    N = 2
    arr = ['hello', 'world']
    str1 = longestCommonPrefix(arr, N)
    print(str1)
    arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
    N = 4
    str1 = longestCommonPrefix(arr, N)
    print(str1)
