def day_to_year(day):
    """
    Given number of days as input, this function convert and returns the
    days into years, month and remaining days.
    """
    year = day // 365
    day = day % (year * 365)
    month = day // 30
    day = day % (month * 30)

    return f"{year} years, {month} months and {day} days"


print(day_to_year(4320))
print(day_to_year(4000))

# print(day_to_year.__doc__)   # Access Docstring
