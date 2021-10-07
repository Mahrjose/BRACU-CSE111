def str_sort(str):
    """
    Given string as input, this function print a sorted version of
    that string. The sorting is done in the following manner:
          1. All sorted lowercase letters are ahead of uppercase letters.
          2. All sorted uppercase letters are ahead of digits.
          3. All sorted odd digits are ahead of sorted even digits.
    """
    low_str, up_str, num_odd, num_even = "", "", "", ""
    for char in str:
        if char.islower():
            low_str += char
        if char.isupper():
            up_str += char
        if char.isdigit():
            if char in ["1", "3", "5", "7", "9"]:
                num_odd += char
            else:
                num_even += char

    sorted_char = sorted(low_str)
    low_str = "".join(sorted_char)

    sorted_char = sorted(up_str)
    up_str = "".join(sorted_char)

    sorted_char = sorted(num_odd)
    num_odd = "".join(sorted_char)

    sorted_char = sorted(num_even)
    num_even = "".join(sorted_char)

    sorted_str = low_str + up_str + num_odd + num_even
    print(sorted_str)


unsorted = input()
str_sort(unsorted)
