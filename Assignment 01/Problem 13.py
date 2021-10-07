# Problem -1


def combine_dictionaries(dict_1, dict_2):
    """
    Given two dictionaries, this function returns a new dictionary
    combining the two input dictionaries and adding the values for
    the common key.
    """
    combined_dict = {}

    for key in dict_1:
        if key in dict_2:
            new_value = dict_1[key] + dict_2[key]
        else:
            new_value = dict_1[key]

        combined_dict[key] = new_value

    for key in dict_2:
        if key not in combined_dict:
            combined_dict[key] = dict_2[key]

    return combined_dict


str_input_1 = input()  # "a: 100, b: 100, c: 200, d: 300" #Question Example Inputs
str_input_2 = input()  # "a: 300, b: 200, d: 400, e: 200" #Question Example Inputs

dict_1 = dict(
    (x.strip(), int(y.strip()))
    for x, y in (element.split(":") for element in str_input_1.split(", "))
)

dict_2 = dict(
    (x.strip(), int(y.strip()))
    for x, y in (element.split(":") for element in str_input_2.split(", "))
)

result = combine_dictionaries(dict_1, dict_2)
unique_value = tuple(
    sorted(set(result[value] for value in result))
)  # Made set for removing all the duplicate, then sorted and made into a tuple.
print(result)
print(f"Values: {unique_value}")
