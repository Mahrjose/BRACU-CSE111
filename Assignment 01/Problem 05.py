def common_char(input_list):
    """
    Given two strings, this function prints a new string with
    the common characters of the origal two string.
    """
    if len(input_list[0]) < len(input_list[1]):
        ref_str = input_list[1]
        str_var = input_list[0]
    else:
        ref_str = input_list[0]
        str_var = input_list[1]

    new_str = ""
    for i in str_var:
        if i in ref_str:
            new_str += i

    for i in ref_str:
        if i in str_var:
            new_str += i

    if new_str == "":
        print("Nothing in common")
    else:
        print(new_str)


user_input = input().split(",")
common_char(user_input)

# print(common_char.__doc__)   # Acess Docstring.
