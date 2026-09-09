total_r = int(input("Enter number of rows: "))

for r in range(total_r):
    curr_letter = chr(65 + r)
    print((curr_letter + " ") * (r + 1))
