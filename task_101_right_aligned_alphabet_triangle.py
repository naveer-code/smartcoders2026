n_rows = int(input("Enter number of rows: "))

for r in range(1, n_rows + 1):
    padding = "  " * (n_rows - r)
    letters = [chr(65 + i) for i in range(r)]
    print(padding + " ".join(letters) + " ")
