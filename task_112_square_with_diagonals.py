dim_size = int(input("Enter size (e.g. 5): "))

for r in range(dim_size):
    output_cells = []
    for c in range(dim_size):
        border = (r == 0 or r == dim_size - 1 or c == 0 or c == dim_size - 1)
        diag = (r == c or r + c == dim_size - 1)
        output_cells.append("*" if (border or diag) else " ")
    print(" ".join(output_cells) + " ")
