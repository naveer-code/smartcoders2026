limit_r = int(input("Enter number of rows: "))

for row in range(1, limit_r + 1):
    line = [str(k) for k in range(1, row + 1)]
    print(" ".join(line) + " ")
