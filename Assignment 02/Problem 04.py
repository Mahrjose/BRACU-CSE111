def foodpanda(food, location="Mohakhali"):
    """
    Given food name and location, this function calculates
    the total price for the food order and returns the
    total price.
    """
    if location != "Mohakhali":
        delivery_charge = 60
    else:
        delivery_charge = 40

    if food == "BBQ Chicken Chesse Burger":
        meal_cost = 250
    elif food == "Beef Burger":
        meal_cost = 170
    elif food == "Naga Drums":
        meal_cost = 200
    else:
        return "The food is not on the Menu."

    tax = meal_cost * (8 / 100)

    Total_Price = meal_cost + delivery_charge + tax
    return Total_Price


print(foodpanda("Beef Burger", "Dhanmondi"))
print(foodpanda("Beef Burger"))

# food = input()
# location = input()

# if location != "":
#    print(foodpanda(food, location))
# else:
#    print(foodpanda(food))

# print(foodpanda.__doc__)   # Access Docstring
