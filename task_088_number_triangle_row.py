n_lines = int(input("Enter number of rows: "))

for r in range(1, n_lines + 1):
    row_str = " ".join([str(r)] * r)
    print(row_str + " ")
