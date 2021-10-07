def ispalindrome(word):
    """
    Given a string as input, this function checks wheater
    the string is a palindrome or not. If yes, it prints
    "Palindrome" otherwise "Not a palindrome".
    """
    string = ""
    for char in word:
        if char != " ":
            string += char

    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


word = input().lower()
ispalindrome(word)

# print(ispalindrome.__doc__)   # Access Docstring
