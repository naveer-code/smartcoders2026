b_size = int(input("Enter half rows (e.g. 4): "))

for i in range(1, b_size + 1):
    w = "*" * i
    g = " " * (2 * (b_size - i))
    print(w + g + w)

for i in range(b_size, 0, -1):
    w = "*" * i
    g = " " * (2 * (b_size - i))
    print(w + g + w)
