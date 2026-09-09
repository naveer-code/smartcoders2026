depth_rows = int(input("Enter number of rows: "))

for r in range(1, depth_rows + 1):
    for c in range(r):
        print(1 if (c % 2 == 0) else 0, end=" ")
    print()
