member_count, times = tuple(int(num) for num in input().split())
joined_data = [int(i) for i in input().split()]

while len(joined_data) != member_count:
    print(
        "Member count and member participation data doesn't match. Please enter member participation data again."
    )
    joined_data = [int(i) for i in input().split()]

approved = [int(i) for i in joined_data if (i + times <= 5)]

appr = len(approved)

if appr < 3:
    print(0)
else:
    if appr % 3 == 0:
        print(appr // 3)
    elif (appr - 1) % 3 == 0:
        print((appr - 1) // 3)
    elif (appr - 2) % 3 == 0:
        print((appr - 2) // 3)
