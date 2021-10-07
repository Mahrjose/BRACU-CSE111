def vowel(string):
    """
    Given a string, this function search for any vowels in the given string
    and returns the founded vowels and the vowel count as output. If no
    vowel found, it returns "No vowels in the name".
    """
    vowel = "aeiouAEIOU"
    vowel_in, total = "", 0

    for char in string:
        if char in vowel:
            vowel_in += char + ", "
            total += 1

    if total == 0:
        return "No vowels in the name"
    else:
        return f"Vowels: {vowel_in[:-2]}. Total number of vowels: {total}"


print(vowel("Steve Jobs"))
print(vowel("XYZ"))
print(vowel("Anime"))
print(vowel("AeIoU"))

# print(vowel.__doc__)   # Acess Docstring.
