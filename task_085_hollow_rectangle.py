h_rows = int(input("Enter rows: "))
w_cols = int(input("Enter columns: "))

for r in range(h_rows):
    if r == 0 or r == h_rows - 1:
        print("* " * w_cols)
    else:
        print("*" + " " * (2 * w_cols - 3) + "*")
