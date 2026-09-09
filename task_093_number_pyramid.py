n_h = int(input("Enter number of rows: "))

for r in range(1, n_h + 1):
    space_prefix = "  " * (n_h - r)
    digits = [str(x) for x in range(1, 2 * r)]
    print(space_prefix + " ".join(digits) + " ")
