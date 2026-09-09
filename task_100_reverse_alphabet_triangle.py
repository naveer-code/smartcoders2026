span_r = int(input("Enter number of rows: "))

for length in range(span_r, 0, -1):
    for j in range(length):
        print(chr(65 + j), end=" ")
    print()
