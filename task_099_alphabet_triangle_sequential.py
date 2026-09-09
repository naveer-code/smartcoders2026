count_r = int(input("Enter number of rows: "))

for r in range(1, count_r + 1):
    for c in range(r):
        print(chr(ord('A') + c), end=" ")
    print()
