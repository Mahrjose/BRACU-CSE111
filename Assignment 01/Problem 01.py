def case_converter(string):
    """
    Given string as input, if string has more uppercase letters
    than lowercase print string in all uppercase. Otherwise, does
    the oppsite.
    """
    # We can get the uppercase and lowercase letter count by this method. But using map and sum is more cleaner method.
    #
    # lower_case = ""
    # upper_case = ""
    # for char in string:
    #    if ord(char) >= 65 and ord(char) <= 90:
    #        upper_case += char
    #    else:                      #Since input only contains uppercase and lowercase, checking one condition should be enough.
    #        lower_case += char
    #
    # total_lower = len(lower_case)
    # total_upper = len(upper_case)

    total_lower = sum(map(str.islower, string))
    total_upper = sum(map(str.isupper, string))

    if total_upper > total_lower:
        return string.upper()
    else:
        return string.lower()


user_input = input()
result = case_converter(user_input)
print(result)

# print(case_converter.__doc__)   # Access docstring
