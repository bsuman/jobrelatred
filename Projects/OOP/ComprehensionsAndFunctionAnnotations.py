# list comprehension with the if operator
list_x = [i for i in range(1, 10) if i % 2 == 0]
print(list_x)

# nest list comprehension
matrix = [[j + 1 for j in range(1, 4)] for i in range(0, 3)]
print(matrix)

dict = {}
for i in range(65, 91):
    dict[i] = chr(i)
# accessing items in dictionary
for k, v in dict.items():
    print("Key:{}, Value:{}".format(k, v))

# accessing the enumeration (index) and the value using enumerate function
list_ex = [chr(i) for i in range(65, 91)]
for e, i in enumerate(list_ex):
    print("Enumeration:{}, Value: {}".format(e, i))

# using zip function, looping over two lists or iterables at the same time
# it can be used in non-strict mode i.e. loop runs until the shortest list is iver
list_y = [month for month in range(1, 13)]
# runs 12 times
for x, y in zip(list_y, list_ex):
    print("Month:{}, Alphabets:{}".format(x, y))


# if used in strict mode, the zip function throws value error that the given iterables are not of the same length

# all methods that can be applied on lists can be used while looping over them : example: reverse, sorted


# function annotations:
# function definition done with keyword def
# all local variables are included the local symbol table
# lookup order of the variables used in the function (LEGB) :
# 1. local symbol table for the function
# 2. enclosing function symbol table
# 3. global symbol table
# 4. built-in symbol table

# default return value of all functions in python unless defined by user otherwise is NONE i.e. why it is a function and not a procedure
# default values for the arguments are done by using = sign between the argument and the default value
# Rule: default arguments are evaluated only once during the definition of the call
# Mutable objects should not be used as default value because they are evaluated once and between the function calls not reassigned the value

def check_list(value, mut_object=[]):
    mut_object.append(value)
    return mut_object


print(check_list(1))
print(check_list(2))  # expected [2] but result = [1,2]
print(check_list(3))  # expected [3] but result = [1,2,3]


# correct way of the assigning default value to an argument which is to be used for mutable object:

def check_list_correct(value, mut_object=None):
    if mut_object is None:
        mut_object = []
    else:
        mut_object.append(value)
    return mut_object


print(check_list_correct(1))  # expected [] but result = []
print(check_list_correct(2, []))  # expected [2] but result = [2]
print(check_list_correct(3, []))  # expected [3] but result = [3]

# during the function call, the resolution of the argument assignment can be :
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# 1. positional:order of the input arguments decided the assignment ( to mark all the arguments until / as positional)
# 2. keyword arguments: matching keyword name to value ( order does not matter and keyword name should match one of the function arguments)
# (to mark all the arguments after * as keyword)
# 3. *args: argument is a pointer to a list all the arguments to the function ( variadic arguments)

# generator functions
# returns generator object with the output and the object content need to be accessed via for loop
gen_tmp = (n*n for n in range(1,10))
for i in gen_tmp:
    print(i)