class Wadiya:
    def __init__(self):
        self.name = "Aladeen"
        self.designation = "President Prime Minister Admiral General"
        self.num_of_wife = 100
        self.dictator = True


wadiya = Wadiya()
print("Part 1:")
print(f"Name of President: {wadiya.name}")
print(f"Designation: {wadiya.designation}")
print(f"Number of wife: {wadiya.num_of_wife}")
print(f"Is he/she a dictator: {wadiya.dictator}")
print("=====================")
# ==================================================================== #
# Changing values
wadiya.name = "Donald-Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = False
# ==================================================================== #
print("Part 2:")
print(f"Name of President: {wadiya.name}")
print(f"Designation: {wadiya.designation}")
print(f"Number of wife: {wadiya.num_of_wife}")
print(f"Is he/she a dictator: {wadiya.dictator}")
print("=====================")
print("privious information lost")
