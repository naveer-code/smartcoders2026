n_levels = int(input("Enter number of rows: "))

for r in range(1, n_levels + 1):
    line_bits = [str(i % 2) for i in range(r)]
    print(" ".join(line_bits) + " ")
