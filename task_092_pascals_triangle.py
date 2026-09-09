import math

n_rows = int(input("Enter number of rows: "))

for r in range(n_rows):
    indent = " " * (n_rows - r - 1)
    line_nums = [str(math.comb(r, c)) for c in range(r + 1)]
    print(indent + " ".join(line_nums) + " ")
