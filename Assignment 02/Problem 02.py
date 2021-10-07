def BMI_Calc(height, weight):
    """
    Given height and weight as input, this function
    calculate the BMI of a person with the following
    formula:
            BMI = Kg / 𝑚^2
    Then it returns the BMI and the following comment
    based on BMI score:
            * < 18.5 - Underweight
            * 18.5 - 24.9 - Normal
            * 25 - 30 - Overweight
            * > 30 - Obese
    """
    height = height / 100  # Converting cm to meter
    BMI = weight / height ** 2

    if BMI < 18.5:
        comment = "Underweight"
    elif BMI >= 18.5 and BMI <= 24.9:
        comment = "Normal"
    elif BMI >= 25 and BMI <= 30:
        comment = "Overweight"
    elif BMI > 30:
        comment = "Obese"

    return f"Score is {BMI:.1f}. You are {comment}"


print(BMI_Calc(175, 96))
print(BMI_Calc(152, 48))

# height = int(input())
# weight = int(input())
# print(BMI_Calc(height, weight))

# print(BMI_Calc.__doc__)   # Access Docstring
