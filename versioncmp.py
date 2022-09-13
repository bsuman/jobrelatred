def compare_versions(version1,version2):
    verlist1 = version1.split('.')
    verlist2 = version2.split('.')

    l1 = len(verlist1)
    l2 = len(verlist2)
    shortlist = 0
    if l1 >= l2:
        shortlist = l2
    else:
        verlist1.append(0)
        l1 = len(verlist1)
        shortlist = l1

    for i in range(shortlist):
        if int(verlist1[i]) < int(verlist2[i]):
            return False
    return True


if __name__ == '__main__':
    res = compare_versions("11", "10" )
    print(res)

    res = compare_versions("11", "11" )
    print(res)

    res = compare_versions("10.4.6", "10.4")
    print(res)

    res = compare_versions("10.4", "10.4.8",)
    print(res)

    res = compare_versions("10.4", "11",)
    print(res)

    res = compare_versions("10.4", "10.10",)
    print(res)

    res = compare_versions("10.4.9", "10.5")
    print(res)


