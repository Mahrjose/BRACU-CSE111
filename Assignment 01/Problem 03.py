def lower_substr(string):
    """
    Given a string with two uppercase characters, prints the lowercase characters
    between the two uppercase characters.
    """
    upper_count = sum(map(str.isupper, string))
    if upper_count == 2:
        for i in string:
            if i.isupper():
                start = string.find(i)
                new_str = string.replace(i, i.lower())
                break

        for i in new_str:
            if i.isupper():
                end = new_str.find(i)
                break

        var = string[start + 1 : end]
        if var != "":
            print(var)
        else:
            print("BLANK")

    else:
        print("More than 2 uppercase chracters")


user_input = input()
lower_substr(user_input)
