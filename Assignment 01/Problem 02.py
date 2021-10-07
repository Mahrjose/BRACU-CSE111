def char_checker(string):
    """
    Check wheater a string is number, word or mixed with digits and letters.
    """
    ref_str = "0123456789"
    len_str = len(string)
    count = 0

    for i in string:
        if i in ref_str:
            count += 1

    if count == 0:
        print("WORD")
    elif count < len_str:
        print("MIXED")
    elif count == len_str:
        print("NUMBER")


user_input = input()
char_checker(user_input)
