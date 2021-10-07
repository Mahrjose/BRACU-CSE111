def input_frequency(number):
    """
    Given a number string as input, this function convert the string
    into an integer and add the integer to the list named "ref_list".
    Then it returns a dictionary with the integer as its "key" and
    how many times the integer repeated itself in the "ref_list as
    its value.
    """
    global ref_list
    temp = [int(number)]
    ref_list += temp
    frequency = dict((num, ref_list.count(num)) for num in ref_list)
    return frequency


user_input = input()
ref_list = []
while user_input != "STOP":
    result = input_frequency(user_input)
    user_input = input()

inpt = result.keys()
inpt = sorted(inpt)

for i in inpt:
    print(f"{i} - {result[i]} times")
