# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
#
# The string has the following conditions to be alphanumeric:
#
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore


def alphanumeric(password):
    allowedchar = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if password == "":
        return False
    else:
        chk = password.lower()
        for i in chk:
            if i in allowedchar:
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    print(alphanumeric("PassW0rd"))
