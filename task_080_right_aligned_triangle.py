r_num = int(input("Enter number of rows: "))
for k in range(1, r_num + 1):
    print(f"{' ' * (r_num - k)}{'*' * k}")
