def find_duplicates(arr1, arr2):
    finlist = []

    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1

    index1 = 0
    index2 = 0
    while index2 < len(arr2) and index1 < len(arr1):
        if arr2[index2] == arr1[index1]:
          finlist.append(arr2[index2])
          index2+=1
          index1+=1
        elif arr2[index2] < arr1[index1]:
          while index2 < len(arr2) and arr2[index2] < arr1[index1]:
            index2 +=1
        elif arr1[index1] < arr2[index2]:
          while index1 < len(arr1) and arr1[index1]< arr2[index2]:
            index1 +=1
    return finlist

if __name__ == '__main__':
    arr1 = [1,3,5,9]
    arr2 = [2,4,6,10]
    print(find_duplicates(arr1,arr2))