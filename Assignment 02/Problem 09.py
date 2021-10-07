def capitalize(string):
    """
    Given a string with incorrect caplitalization, this
    function correctly capitalize the string and then
    returns it.
    """
    if string != "":
        if string[0] >= chr(97) and string[0] <= chr(122):
            capitalized_str = chr(ord(string[0]) - 32)
        else:
            capitalized_str = string[0]

        for index in range(1, len(string)):
            if (
                string[index - 1] == " "
                and string[index] == "i"
                and string[index + 1] == " "
            ):
                capitalized_str += "I"

            elif (
                string[index - 2] == "."
                or string[index - 2] == "!"
                or string[index - 2] == "?"
            ):
                capitalized_str += chr(ord(string[index]) - 32)

            else:
                capitalized_str += string[index]

        return capitalized_str

    else:
        return "Please enter a valid string."


print(
    capitalize(
        "my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much."
    )
)

print(capitalize(""))

# print(capitalize.__doc__)   # Access Docstring
