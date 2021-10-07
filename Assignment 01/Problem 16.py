def count_dict(string):
    """
    Given a string, this function returns a dictionary containing
    the characters of the string as "key" and how many times the
    character repeated itself as a value.
    """
    dictionary = {}

    for char in string:
        if char == " ":
            continue
        dictionary[char] = dictionary.get(char, 0) + 1

    return dictionary


user_input_1 = input()
user_input_2 = input()

dict_1 = count_dict(user_input_1)
dict_2 = count_dict(user_input_2)

if user_input_1 != user_input_2:
    if dict_1 == dict_2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")
else:
    print("Those strings are not anagrams.")
