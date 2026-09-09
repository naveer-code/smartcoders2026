sz = int(input("Enter odd size (e.g. 5): "))

for r in range(sz):
    row_symbols = []
    for c in range(sz):
        row_symbols.append("*" if (r == c or r + c == sz - 1) else " ")
    print(" ".join(row_symbols) + " ")
