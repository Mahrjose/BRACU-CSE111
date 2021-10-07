def key_map(string):
    """
    Given a string, this function retruns the key presses needed 
    for that string to be entered on some basic cell phones.
    """
    key_map = {
        ".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
        "A": 2, "B": 22, "C": 222,
        "D": 3, "E": 33, "F": 333,
        "G": 4, "H": 44, "I": 444,
        "J": 5, "K": 55, "L": 555,
        "M": 6, "N": 66, "O": 666,
        "P": 7, "Q": 77, "R": 777, "S": 7777,
        "T": 8, "U": 88, "V": 888,
        "W": 9, "X": 99, "Y": 999, "Z": 9999,
        " ": 0
    }
    map = {2: "ABC", 3: "DEF"}
    

    return key_map.get(string, f"(No-Key-For:{string})")

user_input = input().upper()
for char in user_input:
    key = key_map(char)
    print(key, end="")
