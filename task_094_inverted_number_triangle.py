max_r = int(input("Enter number of rows: "))

for length in range(max_r, 0, -1):
    for v in range(1, length + 1):
        print(v, end=" ")
    print()
