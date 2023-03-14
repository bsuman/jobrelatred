def remove_duplicates_numlist(nums):
    finalist = []
    dict_num = {}
    for num in nums:
        if num not in dict_num.keys():
            finalist.append(num)
            dict_num[num] = True
    nums[:] = finalist
    return nums

if __name__ == "__main__":
    nums = [1,2,3,2,3,5,4,5,32,4,5]
    print(remove_duplicates_numlist(nums))