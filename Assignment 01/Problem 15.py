def invert(dictionary):
    """
    Given a dictionary as input, this function returns a new dictionary
    with the "value" of the first dictionary as its "key" and a list of
    "key" from the first dictionary as its "value".
    """
    Dict = {}
    for item1, item2 in dictionary.items():
        if item2 in Dict:
            Dict[item2] = Dict[item2] + [item1]
        else:
            Dict[item2] = [item1]

    return Dict


str_input = (
    input()
)  # "Key1 : value1, Key2 : value2, key3 : value1" #Question Input Example

dictionary = dict(
    (x.strip(), y.strip())
    for x, y in (item.split(":") for item in str_input.split(", "))
)

result = invert(dictionary)
print(result)
