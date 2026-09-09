size_h = int(input("Enter half rows (e.g. 4): "))

for r in range(size_h, 1, -1):
    print(" " * (size_h - r) + "*" * (2 * r - 1))

for r in range(1, size_h + 1):
    print(" " * (size_h - r) + "*" * (2 * r - 1))
