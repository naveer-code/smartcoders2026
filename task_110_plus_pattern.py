sz = int(input("Enter odd size (e.g. 5): "))

midpoint = sz // 2
for r in range(sz):
    row_data = ["*" if (r == midpoint or c == midpoint) else " " for c in range(sz)]
    print(" ".join(row_data) + " ")
