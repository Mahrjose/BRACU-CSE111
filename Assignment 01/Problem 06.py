def is_Spec_Char(character):
    """
    Given a character, this function checks wheater a character is
    one of the four special characters.
    """
    spec_char = "_$#@"
    if character in spec_char:
        return True
    else:
        return False


def password_checker(password):
    """
    Given a password as string, this function checks wheater the password
    fulfills the four requirements :
                1. At least one lowercase letter
                2. At least one uppercase letter
                3. At least one digit (0-9)
                4. At least one special character (_,$,#,@)
    If the password does not fulfill the requirements if returns one of the
    four specific errors. Otherwise, if all the reqirments are met, it
    returns "OK".
    """
    lower_count = sum(map(str.islower, password))
    upper_count = sum(map(str.isupper, password))
    digit_count = sum(map(str.isdigit, password))
    spec_count = sum(map(is_Spec_Char, password))

    error = ""
    if lower_count == 0:
        error = "Lowercase Chracter Missing"

    if upper_count == 0:
        if error != "":
            error += ", "
        error += "Uppercase Chracter Missing"

    if digit_count == 0:
        if error != "":
            error += ", "
        error += "Digit Missing"

    if spec_count == 0:
        if error != "":
            error += ", "
        error += "Special Chracter Missing"

    if error == "":
        print("OK")
    else:
        print(error)


password = input()
password_checker(password)

# print(password_checker.__doc__)   # Acess Docstring
