def UB_Jupmer(List):
    """
    Given a list as input, this function returns True if the input
    list is a UB Jumper or return False otherwise.
    """
    ref_list = [num for num in range(1, len(List))]
    abs_diff = []

    for i in range(len(List) - 1):
        elem = List[i] - List[i + 1]
        elem = abs(elem)
        abs_diff.append(elem)

    if sorted(ref_list) == sorted(abs_diff):
        return True
    else:
        return False


user_input = input()
result = []
while user_input != "STOP":
    List = [int(num) for num in user_input.split()]

    if UB_Jupmer(List):
        result.append("UB Jumper")
    else:
        result.append("Not UB Jumper")

    user_input = input()

for output in result:
    print(output)
