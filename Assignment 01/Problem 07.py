def universal_list(number):
    """
    Given number as string input, this function convert the string
    into an integer and add the integer to the List named "ref_list".
    """
    global ref_list
    temp = [int(number)]
    ref_list += temp


user_input = input()
ref_list = []
while user_input != "STOP":
    universal_list(user_input)
    user_input = input()


frequency = [[num, ref_list.count(num)] for num in ref_list]
frequency = sorted(
    frequency, key=lambda x: x[0]
)  # Sorting the frequency list by the first element (number) the of the sublist

sorted_frequency = []
[
    sorted_frequency.append(item) for item in frequency if item not in sorted_frequency
]  # Creating a list with unique items

for inpt, outpt in sorted_frequency:
    print(f"{inpt} - {outpt} times")
