n_lines = int(input("Enter number of rows: "))

for r in range(n_lines, 0, -1):
    for c in range(r, 0, -1):
        print(c, end=" ")
    print()
