def sum_list(lst):
    """
    Given a list as input, this function checks wheater the sum of given
    list is maximum among the input lists.
    """
    global max_sum, max_lst
    lst_sum = sum(lst)
    if lst_sum > max_sum:
        max_sum = lst_sum
        max_lst = lst


N = int(input())
max_sum = 0
max_lst = []
for i in range(N):
    lst = [int(num) for num in input().split()]
    sum_list(lst)

print(max_sum)
print(max_lst)
