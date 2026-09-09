half_h = int(input("Enter half rows (e.g. 4): "))

for top in range(1, half_h + 1):
    print(f"{' ' * (half_h - top)}{'*' * (2 * top - 1)}")

for bot in range(half_h - 1, 0, -1):
    print(f"{' ' * (half_h - bot)}{'*' * (2 * bot - 1)}")
