def div_frac(numerator, denominator):
    """
    Given two numbers as input, this function divide one
    number by another and returns the the fraction part of
    the result.

    Exception: if the denominator is 0 then it returns 0.
    """
    if denominator == 0:
        return 0
    else:
        result = (numerator / denominator) - (numerator // denominator)
        if result == 0.0:
            return 0
        else:
            return result


print(div_frac(5, 2))
print(div_frac(5, 0))
print(div_frac(0, 5))

# print(div_frac.__doc__)   # Access Docstring
