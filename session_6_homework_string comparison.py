# python 3

# ------------------  HOMEWORK SESSION 6  ------------------

# Do not use the built-in string compare methods, you are trying to write those library functions.

# define boolean function compare(one : string, two : string, caseInsensitive : boolean)
#
# compare("hello", "hello", false) -> true
# compare("hello", "hello", true) -> true
# compare("hello", "HELLO", false) -> false
# compare("hello", "HELLO", true) -> true


def compare_str(str1, str2, case_insensitive):
    """

    :param str1: string where len(str1) = len(str2)
    :type str1: string
    :param str2: string where len(str1) = len(str2)
    :type str2: string
    :param case_insensitive: if True, does not compare if upper or lower case
    :type case_insensitive: Boolean
    :return: True or False
    :rtype: Boolean
    """

    for i in range(len(str1)):
        char1, char2 = str1[i], str2[i]
        if case_insensitive:
            if char1.lower() != char2.lower():
                return False
        else:
            if char1 != char2:
                return False
    return True


print(compare_str("hello", "hello", False))  # -> true
print(compare_str("hello", "hello", True))   # -> true
print(compare_str("hello", "HELLO", False))  # -> false
print(compare_str("hello", "HELLO", True))   # -> true
