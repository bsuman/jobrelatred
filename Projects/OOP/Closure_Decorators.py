# example for implementation of decorators
# implementing a decorator class which can be used the log function name and arguments to the console before calling the function
class dummy_deco:
    def __init__(self, myfunc):
        self.function = myfunc

    def __call__(self, *args, **kwargs):
        print("Calling function \"{}\" with function arguments {}".format(self.function.__name__, args))
        return self.function(*args, **kwargs)


@dummy_deco
def display(name, age):
    print("My name is {} and I am {} years old".format(name, age))


@dummy_deco
def add(x, y):
    print("After addition, value is {}".format(x + y))


display("Suman", "34")
add(10, 15)
