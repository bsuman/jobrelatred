# example to understand how to create user-defined exceptions
# Implement a class to created dictionary which takes only key and values of string type
# In case of correct type of key value provided, it stores the value
# otherwise it raises a user-defined ValueTypeError

class ValueTypeError(Exception):
    def __init__(self, key=None, value=None, message="Only string type allowed for key and value"):
        self.key = key
        self.value = value
        self.message = message

    def __str__(self):
        if self.key is not None and self.value is not None:
            return "The key {0}, value {1} of type {2}, type{3} is incorrect".format(self.key, self.value,
                                                                                     type(self.key), type(self.value))
        else:
            return self.message


class strdict:
    empty_dict = {}

    def __init__(self, key, value):
        if key is not None and value is not None:
            self.addValue(key, value)

    def addValue(self, key, value):
        try:
            if not isinstance(key, str):
                raise ValueTypeError(key, value)
            elif not isinstance(value, str):
                raise ValueTypeError(key, value)
        except ValueTypeError as typeError:
            print(typeError)
        else:
            self.empty_dict[key] = value

    def get_keys(self):
        return self.empty_dict.keys()

if __name__ == '__main__':
    test_1 = strdict('str1','val1')
    print(test_1.get_keys())
    test_1.addValue(8,'tmp1')
    test_1.addValue('tmp1', 12.3)
    test_1.addValue(None, 'tmp1')
    test_1.addValue('tmp1', None)
    test_1.addValue('tmp1', 'tmp2')
    print(test_1.get_keys())
