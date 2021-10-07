def replace_word(string):
    """
    Given a string, this function search for the substring "too good".
    If it find that, then replaces the substring with another substring
    "execellent" and returns the modified string. Otherwise, it returns
    the original string
    """
    # We can do the program like below which don't use replace method. Or, we can just use find and replace method.
    #
    # replaced_str = ""
    # pos = -1
    # for i in range(len(string)):
    #    if string[i] == "t" and string[i + 1] == "o" and string[i + 2] == "o" and string[i + 3] == " " and string[i + 4] == "g" and string[i + 5] == "o" and string[i + 6] == "o" and string[i + 7] == "d":
    #        pos = i
    #        break
    #
    #
    # if pos != -1:
    #    replaced_str = string[:pos] + "execellent" + string[pos + len("too good"):]
    #    print(replaced_str)
    # elif pos == -1:
    #    print(string)

    pos = string.find("too good")
    if pos == -1:
        print(string)
    elif pos != -1:
        new_str = string.replace("too good", "execellent")
        print(new_str)


user_name = input()
replace_word(user_name)

# print(replace_word.__doc__)   # Access Docstring.
