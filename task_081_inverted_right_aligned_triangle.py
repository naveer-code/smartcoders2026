r_num = int(input("Enter number of rows: "))
for k in range(r_num, 0, -1):
    print(f"{' ' * (r_num - k)}{'*' * k}")
