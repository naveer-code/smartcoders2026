h_val = int(input("Enter number of rows: "))

for r in range(1, h_val + 1):
    pad = "  " * (h_val - r)
    asc = [chr(65 + j) for j in range(r)]
    desc = [chr(65 + j) for j in range(r - 2, -1, -1)]
    print(pad + " ".join(asc + desc) + " ")
