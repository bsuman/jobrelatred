# higher order functions example

new_list = [_ for _ in range(1, 11)]
print(new_list)
pow_2_list = list(map(lambda x: x * x, new_list))
print(pow_2_list)

newset = set(_ for _ in range(65, 91))
upper_2_set = set(map(lambda x: chr(x).upper(), newset))
print(upper_2_set)

upper_2_list = list(map(lambda x: chr(x).upper(), newset))
print(upper_2_list)
print(newset)


# TypeError: 'NoneType' object is not callable
# test = list(map(None,newset))
# print(test)

# using doc string
def double_num(i):
    """
    :param i: input number to be doubled
    :return: doubled value of the input number
    """
    return i * 2


# passing a non-lambda function as an argument
double_ls = list(map(double_num, new_list))
print(double_ls)

is_vowel_ascii_code = list(filter(lambda x: chr(x) in ['A', 'I', 'E', 'O', 'U'], newset))
print(is_vowel_ascii_code)

is_vowel = list(filter(lambda x: x in ['A', 'I', 'E', 'O', 'U'], upper_2_list))
print(is_vowel)

# identity function used as default when the function passed is None
test = list(filter(None, newset))
print(test)
