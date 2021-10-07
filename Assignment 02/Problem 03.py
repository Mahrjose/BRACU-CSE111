def div_sum(min, max, div):
    """
    This function takes 3 number maximum, minimum and divisor
    as input. Then it finds all the number divisible by the
    divisor between minimum and maximum value. Then it returns
    the sum of these number.
    """
    if div != 0:

        # Without using sum()
        # Sum = 0
        # for num in range(min, max):
        #    if num % div == 0:
        #        Sum += num
        # return Sum

        return sum(num for num in range(min, max) if num % div == 0)

    else:
        return "Divisor cannot be 0."


print(div_sum(0, 10, 2))
print(div_sum(3, 16, 3))
print(div_sum(1, 15, 0))


# minimum = int(input("Minimum: "))
# maximum = int(input("Maximum: "))
# divisor = int(input("Divisor: "))
# print(div_sum(minimum, maximum, divisor))

# print(div_sum.__doc__)   # Access Docstring
