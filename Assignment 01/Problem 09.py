def list_multiplication(lst_1, lst_2):
    """
    Given two list as input, this function returns a new list
    containing the cross multiplication product between the given
    two lists.
    """
    return [(i * j) for i in lst_1 for j in lst_2]


list_1 = [int(num) for num in input().split()]
list_2 = [int(num) for num in input().split()]
result = list_multiplication(list_1, list_2)
print(result)
